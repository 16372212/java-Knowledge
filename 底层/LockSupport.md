# LockSupport
## 简介

用来创建锁和其他同步类的基本线程**阻塞原语**

## 核心函数

```java
LockSupport.park(boolean isAbsolute, long time): 线程阻塞. time为等待时间，超过时间自动释放锁
LockSupport.unpark: // 不安全，要确保线程依旧存活
```

引入的都是unsafe的park, unpark函数。

## 源码
```java
private LockSupport() {} // Cannot be instantiated.

// 阻塞
public static void park(Object blocker) {
    Thread t = Thread.currentThread();
    setBlocker(t, blocker); // 将线程阻塞
    UNSAFE.park(false, 0L); // 调用park后，无法走下一步（setBlocker(t,null), 直到获得unpark）
    setBlocker(t, null);
}
```

> block, wait区别：block是因为线程等待获取监视器monitor锁以期进入同步代码块/Object.wait, 通过notify可以被唤醒。

## 其他问题

### Thread.sleep() 和 LockSupport.park()的区别

都是阻塞且不会释放锁资源。但是：

1. Thread.sleep()无法从外部唤醒，只能自己醒过来; LockSupport.park()可以被另一个线程调用LockSupport.unpark()
2. Thread.sleep()本身是一个native方法，LockSupport.park()底层是调用unsafe的native方法
3. sleep抛出了中断异常，park的没有

### object.wait()和LockSupport.park()区别

1. Object.wait()方法需要在synchronized中执行，LockSupport.park()在任意地方
2. wait抛出了中断异常，park的没有
3. wait没有超时，只能notify唤醒。park也没有超时，通过unpark唤醒。
4. wait前notify跑出异常，park前unpark不会

> Object的wait： wait()方法必须在当前获取的锁对象上调用。wait()方法调用时，会释放线程获得的锁，wait()方法返回后，线程又会重新试图获得锁，才能继续往后执行。

