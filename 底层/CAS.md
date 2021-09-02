# unsafe

JAVA原子类基于unsafe实现，用于提供不安全操作的方法，例如访问系统内存. 返回数组元素内存大小，返回内存页大小，实现CAS,等，

1. Unsafe类提供了3总CAS方法。compareAndSwapObject, compareAndSwapInt, compareAndSwapLong。底层实现compareAndSwap*完全原子的方法：实现总线锁（后来是缓存锁）

2. 获取内存（数组的偏移，占页大小等）

# AtomicInteger等原子类

> volatile（可见性）+CAS更改数据（原子性）

使用unsafe支持的, 
```java
// automic类：

private volatile int value;

public final int addAndGet(int delta) {
    /**
    这个valueOffset是通过 valueOffset = unsafe.objectFieldOffset
                (AtomicInteger.class.getDeclaredField("value"));得到的
                
                **/
    return unsafe.getAndAddInt(this, valueOffset, delta) + delta;
}
// unsafe.getAndAddInt: 使用自旋CAS来实现的
public final int getAndAddInt(Object var1, long var2, int var4) {
        int var5;
        do {
            var5 = this.getIntVolatile(var1, var2);
        } while(!this.compareAndSwapInt(var1, var2, var5, var5 + var4));

        return var5;
    }
```

因此使用多线程对整数操作时，不用`synchronized void increment(){count++}`就可以实现自增。`count.incrementAndGet();`

## 如何解决CAS的ABA问题

维护一个版本号 + 一个对象的引用

使用盘本好控制，每次建立新的pair作为CAS比较对象。

compareAndSet方法：
```java
Pair<V> current = pair;
        return
        // 引号没变
        expectedReference == current.reference && expectedStamp == current.stamp &&
        ((newReference == current.reference && newStamp == current.stamp) ||
            casPair(current, Pair.of(newReference, newStamp))); // 调用unsafe的CAS方法

```