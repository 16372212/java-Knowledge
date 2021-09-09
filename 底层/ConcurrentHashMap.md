# 实现概览

jdk1.7之前的使用分段锁。jdk1.8用数组+链表+红黑树+CAS原子操作 实现 ConcurrentHashMap

# HashTable
HashTable: synchronized对**整个**对象进行put等修改Hash时，进行加锁

# jdk1.7的策略

在对象中保存了一个Segment数组，将整个Hash表划分成多个分段。每个Segment类似于一个HashTable。

每个Segment通过继承ReentrantLock进行加锁。所以每次锁住的是一个segment。segment数组无法扩容。

## 参数

- concurrencyLevel: 并行级别、并发数、Segment的个数。默认为16.

- initialCapacity：初始容量。整个ConcurrentHashMap的初始容量，实际操作需要平均分给每个Segment

-LoadFactor: 负载因子，默认0.75，给每个segment内部用的。Segment数组无法扩容，但是内部可以扩容。

## 初始化槽ensureSegment

> 并发操作使用CAS进行控制。

ConcurrentHashMap初始化会初始化第一个Segment[0], 对于其他槽，是在插入第一个槽的时候进行的初始化。
因为初始化其他槽的时候，需要用当前的segment[0]处的数组长度和负载因子进行初始化。

但是初始化某个槽segment[k]就涉及到多线程对他初始化。

    首先检查这个segment是否被其他线程初始化了。如果没有，就设置一个while循环，while（没被初始化UNSAFE.getObjectVolatile，就循环内部CAS对segment赋值），直到当前线程成功设置or其他线程成功设置。


## 插入set
初始化得到一个Segment数组`Segment<K, V>s`。Segment[i]默认大小为2

插入节点到表头。

1. hash（key）得到数组中的位置j: hash是32位，又因为concurrencyLevel=16，有16个segment, 因此高4位代表的数组下标。
2. segment内部插入。segment内部是数组+链表。现获取segment独占锁。

> 并发：首先获取内部锁，是利用node=tryLock(), 如果获得成功，就利用scanAndLockForPut循环tryLock获得锁。失败次数超过阈值，就进入lock()阻塞队列等待。

## get

没有加锁

问题：get的时候发生remove or put可能有问题。但是：添加节点是通过加到表头实现的。如果这个时候get操作在链表的遍历中已经到了中间，就不会影响。

volatile关键字可以保证put的时候的可见性。

## 限制

最大的并发度受Segment的个数限制。

# JDK1.8

加锁使用**CAS+Synchronized实现**

容量大小：2的次幂：扩容的时候要保证是2的次幂。因为计算桶的hash值时，需要与容量-1（全1）想与得到。而不是取余。因此需要让容量-1为全1的数。

但是改革之后，计算hash的方法不是这种，而是用前16位与后16位与得到。

## put

找到hash值对应的数组下标。如果数组中这个桶为空，则直接CAS方式插入。如果CAS失败，则进入下一个循环。

1. 首先初始化
2. 判断桶是否是空的，里面链表头指针是null，直接CAS插入`f = tabAt(tab, i = (n - 1) & hash)) == null`表示桶是空的
3. 如果不null，则判断状态是否正在扩容`(fh = f.hash) == MOVED`
4. 判断头指针的hash值是否>0, 是否是链表`(fh = f.hash) >= 0`头节点hash值>0, 所以是链表
5. 是否是红黑树`f instanceof TreeBin`

```java
/** Implementation for put and putIfAbsent */
final V putVal(K key, V value, boolean onlyIfAbsent) {
    if (key == null || value == null) throw new NullPointerException();
    int hash = spread(key.hashCode());
    // 数组长度
    int binCount = 0;
    for (Node<K,V>[] tab = table;;) {
        Node<K,V> f; int n, i, fh;
        // 数组为空，初始化
        if (tab == null || (n = tab.length) == 0)
            tab = initTable();
        // 找hash值对应的桶的下标，如果这个桶是空的，就直接CAS插入
        else if ((f = tabAt(tab, i = (n - 1) & hash)) == null) {
            if (casTabAt(tab, i, null,
                            new Node<K,V>(hash, key, value, null)))
                break;                   // no lock when adding to empty bin
        }
        // 如果桶在的链表的hash值是moved，正在扩容
        else if ((fh = f.hash) == MOVED)
            // 帮助数据迁移
            tab = helpTransfer(tab, f);
        // f是头节点
        else {
            V oldVal = null;
            // 该位置头节点监视
            synchronized (f) {
                if (tabAt(tab, i) == f) {
                    if (fh >= 0) { // 头节点hash值>0, 所以是链表
                        // 用于累加，记录链表的长度
                        binCount = 1;
                        for (Node<K,V> e = f;; ++binCount) {
                            K ek;
                            if (e.hash == hash &&
                                ((ek = e.key) == key ||
                                    (ek != null && key.equals(ek)))) {
                                oldVal = e.val;
                                if (!onlyIfAbsent)
                                    e.val = value;
                                break;
                            }
                            Node<K,V> pred = e;
                            if ((e = e.next) == null) {
                                pred.next = new Node<K,V>(hash, key,
                                                            value, null);
                                break;
                            }
                        }
                    }
                    else if (f instanceof TreeBin) { // 红黑树
                        Node<K,V> p;
                        binCount = 2;
                        // 调用红黑树的插值方法插入新节点
                        if ((p = ((TreeBin<K,V>)f).putTreeVal(hash, key,
                                                        value)) != null) {
                            oldVal = p.val;
                            if (!onlyIfAbsent)
                                p.val = value;
                        }
                    }
                }
            }
            if (binCount != 0) {
                // 判断是否将链表转成红黑树
                if (binCount >= TREEIFY_THRESHOLD)
                    treeifyBin(tab, i); // 如果长度<64, 则数组扩容，否则就转成红黑树
                if (oldVal != null)
                    return oldVal;
                break;
            }
        }
    }
    addCount(1L, binCount);
    return null;
}

```

## 扩容：tryPresize
sizeCtl是啥

未完待续...
