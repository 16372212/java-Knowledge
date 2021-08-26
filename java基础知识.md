
[借鉴自](https://snailclimb.gitee.io/javaguide/#/docs/java/basis/Java%E5%9F%BA%E7%A1%80%E7%9F%A5%E8%AF%86?id=jvm-vs-jdk-vs-jre)

## java基本类型：
    boolean
    char
    long
    short
    int
    float
    double
    byte
所占存储空间大小不变

## java关键字

    abstract	class	extends	final	implements	interface	native
    new	static	strictfp	synchronized	transient	volatile	

### 1. abstract 声明抽象

abstract关键字可以修改类或方法。

abstract类：（为了被子类重写）可以扩展（增加子类），但*不能直接实例化*。abstract方法不在声明它的类中实现，但必须在某个子类中重写。采用 abstract方法的类本来就是抽象类，并且必须声明为abstract。

（抽象类里可以包含静态方法）

### 2. static

    2.1 static 修饰属性：无论一个类生成了多少个对象，所有这些对象共同使用唯一一份静态的成员变量；一个对象改了其他的对象也改了。 ‘类名.成员变量名’的方式来使用

    2.2 static修饰方法： 静态方法只能继承，不能重写。可以不生成实例，直接用类名来调用

不能在静态方法中访问非静态成员变量
可以在非静态方法中访问静态的成员变量。因为非静态变量在创建对象实例时才为变量分配内存和初始化变量值。

    2.3 static修饰代码块
    首先执行静态代码块，然后执行构造方法。静态代码块在类被加载的时候执行

    2.4 static修饰类：
    只能用来修饰内部类，被static所修饰的内部类可以用new关键字来直接创建一个实例，不需要先创建外部类实例。static内部类可以被其他类实例化和引用（即使它是顶级类）。

### 3. synchronized


### 4. final finally finalize

#### final:

- 变量：不能被改写
- 方法：方法不能在子类里重写
- 类：无法被继承

#### finally:

无论是否发生异常，finally代码块中的代码总会被执行。try中如果有return，也会执行finally中的值。会先将try中要return的值存起来。当try和finally里都有return时，会忽略try的return，而使用finally的return。


#### finalize:
垃圾回收器准备释放内存的时候，会先调用finalize(), 在垃圾收集器将对象从内存中清除出去之前做必要的清理工作


### String相关

#### string, stringBuffer, stringBuilder

string本身继承自private. 是final修饰的类, 所以不能被更改。所以是线程安全的。

    string是不能被改写的，因为是通过final来修饰的。但是java 1.5之后可以通过反射来改变。因此String可以保证安全性。

stringBuffer对方法增加了同步锁or对调用的方法加了同步锁

stringBuilder没有对调用方法增加同步锁，所以非线程安全。

区别： StringBuffer, StringBuilder使用字符数组保存字符串char[]。没有用final关键字修饰，所以可变。



## object

所有类的父类。
方法：
getClass, hashcode, equals, toString, wait, notify, notifyAll(此对象监视器上等待的所有线程) finalize, 

## 反射


## 集合(容器)

> java中集合分成两大派生接口，collection和map

- collection: 分成三个子接口：list, set, queue

- map: hashtable, hashMap, sortedMap

### 1 collection

#### list
1. arraylist: 底层用object数组存储，线程不安全。数组特性：插入删除复杂度等，支持快速随机访问。空间上，list列表结尾会预留一定的容量空间。

>同步：ArrayList没有同步方法。如果多个线程同时访问一个List，则必须自己实现访问同步。一种解决方法是在创建List时构造一个同步的List

> 增长方式：ArrayList每次对size增长50%->1.5倍，建立一个新数组，再复制

2. linkedList(双向链表)：底层用双向链表存储。空间上：每个元素都要一部分存指针。

> 同步：线程不安全的，方式同上

3. vector：底层也是对象数组。

> 同步：Vector是线程安全的，性能较ArrayList差

> 扩容方式：每次申请自己现有容量的两倍

#### set

1. hashset：底层hashMap实现的vel

2. linkedHashSet： 能够按照添加的顺序便利

3. TreeSet：能按照添加元素的顺序便利，排序的方式有自然排序和定制排序。

#### queue

1. priorityQueue：二插堆实现，底层用可变长度数组存储。非线程安全，不能存null

2. arrayQueue：可变长度的数组+指针。

### dequeue 双端队列

arrayDeQue, LinkedList的区别：

    1. 虽然都实现了Dequeue接口，但底层逻辑不同：arrayDeque：可变长度的数组+双指针。 linkedList是双链表。

    2. arrayDeque不能存null, linkedList能存null

    3. linkedList因为是链表，每次插入都要申请新的堆空间。


### map

#### 1 hashMap

[参考博文](https://blog.csdn.net/u014532901/article/details/78936283)

非同步的，线程不安全。没有同步代码时，无法让多个线程同时使用；hashmap允许有一个null key, multiple null values

1. 什么是hashMap:

HashMap内部实现是一个桶数组，每个桶中存放着一个单链表的头结点。其中每个结点存储的是一个键值对整体（Entry），HashMap采用拉链法解决哈希冲突（关于哈希冲突后面会介绍）。

2. 操作方法：
当调用put操作时，HashMap计算键值K的哈希值，然后将其对应到HashMap的某一个桶(bucket)上；此时找到以这个桶为头结点的一个单链表，然后顺序遍历该单链表找到某个节点的Entry中的Key是等于给定的参数K；若找到，则将其的old V替换为参数指定的V；否则直接在链表尾部插入一个新的Entry节点。


3. hashMap扩容方式（jdk1.7)

hashMap中的一些参数：
`public HashMap(int initialCapacity(数组大小), float loadFactor（装载因子，扩容阈值) = 0.75 ;`
`初始化容量：16:1<<4`

当map中包含的Node的数量（size) 大于等于threshold = loadFactor * capacity(桶的长度）的时候，且新建的Entry刚好落在一个非空的桶上，此刻触发扩容机制，将其容量扩大为*2倍*。

p.s.: 当size大于等于threshold的时候，并不一定会触发扩容机制.只要有一个新建的Node出现哈希冲突，则立刻resize。

resize时候需要完成新表到旧表的转移（transfer）：遍历旧表中的每个桶节点。这个桶节点就是对应数组index位置的链表的头节点。然后依次使用next的方法遍历这些链表，找到每个节点在新表中对应的新位置并插入。*因此多线程时hashMap是不安全的。因为当多个线程同时transfer, 某个线程t所持有的引用next，也就是下一个需要被转移的节点，可能已经放在新表里了。会出现多个线程对同一链表无限进行链表transfer的操作，极易造成死循环，数据丢失等等*

为什么容量必须是二的n次幂：因为获取对应位置时候，是将哈希值h与桶数组的length-1（全1）进行了一个与操作得出了对应的桶的位置，因此如果不是2的倍数，那len-1就不是全1的。

(1.7使用的是头插法，永远添加到数组的头部位置)


4. hashMap扩容方式（jdk1.8)

(1.8使用的是尾插法，永远添加到数组的头部位置)

参数：`初始化容量`, `集合最大容量`, `负载因子0.75`, `8:链表值超过8变成红黑树`,`6:链表值小于6从红黑树转为链表`。 threshed = 容量*负载因子
（详情请见 [底层/容器源码.md](./底层/容器源码.md)）


当链表长度超过8时，链表转换为红黑树

#### 2 LinkedHashMap: 

继承自hashMap，在此基础上加了一个双链表。保证插入顺序。

改变方法：将Entry本身改了, 增加了before, after。因此进行hashcode，equals时
```java
static class Entry<K,V> extends HashMap.Node<K,V> {
    Entry<K,V> before, after;
    Entry(int hash, K key, V value, Node<K,V> next) {
        super(hash, key, value, next);
    }
}
```
这个双链表，将所有的entry链接起来。因此，迭代的时候，只用迭代双向链表即可，不用遍历整个table。

非同步。同步的方法：`Collections.synchronizedMap(new LinkedHashMap(...))`


#### 3 HashTable

同步的。不能存在null key or null values

> 同步的方式：（读写数据的时候，对整个容器上锁）使用的是synchronized来保证线程安全。效率低，如果多个同时访问同步方法，会产生阻塞or轮询。

#### TreeMap：红黑树

#### CuncurrentHashMap: 分段数组+链表+红黑树
> 同步的方式：（使用分段锁，只锁住了需要被修改的部分）使用 Node数组+ 链表 + 红黑树 实现，并发使用synchronized 和CAS来操作。

#### concurrentHashMap & hashMap & hashTable

- 相同点：concurrentHashMap & hashMap 底层数据结构： 对于java1.8. 采用的是数组+链表/红黑树。

- 不同点：线程安全的方式不同：

 

### hashcode equals

hashcode:确定对象在hash表中的索引位置（将内存地址转化为整数后返回）

equals: 确定两个对象是否真的相等。如果equal，则hashcode也一定相等。如果hashcode相等，则不一定equals



### ++i i++
i = 1
b = ++i; // b = 2, 先i自增，再复制给b
b = i++; // b = 1, 先复制给b, i再自增

## java范型
让类型参数化。参数一旦确定好(具体的类型确定后)，如果类似不匹配，编译器就不通过。


### 范型类：
```java
public class Test<T> {
	T field1;
}
Test<String> test1 = new Test<>();
```
### 范型接口
```
public interface Iterable<T> {
}
```
### 范型方法
```java
public <T> void testMethod(T t){
}
```
> 泛型类中的类型参数与泛型方法中的类型参数是没有相应的联系的, 只和自己的定义有关

### <?>：
Sub 是 Base 的子类，不代表 List<Sub>和 List<Base>有继承关系。

<?>提供了*只读*的功能，也就是它删减了增加具体类型元素的能力，只保留与具体类型无关的功能
因此个人认为，<?>提高了代码的可读性

### 类型擦除

> 类型擦除： Java 在编译期间，所有的泛型信息都会被擦掉. 这也让范型和之前的代码可以兼容了。
```java
List<String> l1 = new ArrayList<String>();
List<Integer> l2 = new ArrayList<Integer>();
		
System.out.println(l1.getClass() == l2.getClass());
// 正确答案是 true。都是List.Class
```
在泛型类被类型擦除的时候，之前泛型类中的类型参数部分如果没有指定上限，如 <T>则会被转译成普通的 Object 类型，如果指定了上限如 <T extends String>则类型参数就被替换成类型上限。

范型会带来一些局限：确定类型之后，如果类型不匹配，编译器就不通过。（例如add（integet）后又add(string)， 这编译器就不通过）。但是可以通过类型擦除绕过这个问题：

```java
List<Integer> list = new ArrayList<>();

list.add(12);
//这里直接添加会报错
list.add("a");
Class<? extends List> clazz = list.getClass();
Method add = clazz.getDeclaredMethod("add", Object.class);
//但是通过反射添加，是可以的
add.invoke(list, "kl");

System.out.println(list);

```
			
> 泛型类或者泛型方法中，不接受 8 种基本数据类型。需要使用*包装类*：Integer List<int> li = new ArrayList<>();	

### 常用的通配符为： T，E，K，V，？
？ 表示不确定的 java 类型
T (type) 表示具体的一个 java 类型
K V (key value) 分别代表 java 键值中的 Key Value
E (element) 代表 Element

## equals
String 中的 equals 方法是被重写过的，因为 Object 的 equals 方法是比较的对象的内存地址，而 String 的 equals 方法比较的是对象的值。

## java的方法

静态方法：可以不实例化。调用方法可以使用 类名.方法名 的方式，也可以使用 对象.方法名 的方式
访问变量只能访问静态成员，不能访问实例成员。

一个方法不能修改一个基本数据类型的参数，而对象引用作为参数就不一样

## 容器相关：

### hashcode & equals:

- equals: 根据两个对象的地址值进行比较（比较引用是否相同）但是String是已经重写了equals,即equals比较的是值，==比较的是地址

- hashcode: 对与对象来说，是本地方法，根据值算出来的（hashmap中的key, or hashset中的对象）

>hashCode() returns an integer value, generated by a hashing algorithm.(根据地址hash出来的一个int 32 位的整型数字)


hashcode 相同-> 再查看equals，相同则相同，不相同则不相同。

### 重写hashcode和equals
为什么要同时重写hashcode和equals，不同时重写会出现哪些问题？

要求相同的对象要保持相同的hashcode

如果只重写equals, 则new出来两个相同的对象，equals判断是客观相等，两个所有属性都相等的对象，但是地址不同。但是由于地址不同，hashcode返回的值是false

导致的问题：例如hashMap 想push一个存在的key, 但是hashMap检测不出key存在，就会push成功 

### equals 和 ==

基本数据类型：比较的都是值

- equals比较的是地址，重写之后比较的是值
- == 比较的是地址

### hashmap的方法：

1. 得到hashmap的key的hashcode
2. 通过（n-1）& hash判断当前元素存放的位置。
3. 位置中若存在元素，则判断元素与要存入的hash & key是否相同，*相同就覆盖*，不相同就通过拉链法解决冲突

后来，当链表长度>8, 则将链表转为红黑树



### TreeSet, TreeMap和LinkedHashMap

TreeSet底层是TreeMap实现的.

TreeMap可以保持key的有序。如果有比较器，就按照比较器的大小进行排序，否则就按照key的顺序。
底层实现：

    插入：首先按照二叉排序树进行插入，根据大小往左往右。然后根据红黑树的规则进行调整，左旋、右旋、着色。

LinkedHashMap是有序的，按照插入顺序进行排序。

### 其他的树的结构和优缺点

二叉排序树：比如红黑树属于二叉排序树

（平衡二叉树）AVL: 左右两个子树的高度差的绝对值不超过1，并且左右两个子树都是一棵平衡二叉树

堆：左右两个节点都小于根结点。

最优二叉树：从根结点到各个内结点的加权路径长度之和最小的二叉树


Object都有哪些方法

如何对String进行改写