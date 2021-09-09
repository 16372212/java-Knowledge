# 基本结构

RetrantLock实现了lock接口。

里面包含三个内部类：

1. `abstract static class Sync extends AbstractQueuedSynchronizer`；
2. `static final class NonfairSync extends Sync` 实现了Sync中的lock方法
3. `static final class FairSync extends Sync` 实现了Sync中的lock方法

根据参数决定构造的是公平还是非公平（NonfairSync 还是 FairSync）


## 1 sync源码
维护了一个基本的同步操作：`nonfairTryacquire`, `tryRelease`。用AQS的state代表拥有锁的进程个数。

### 1.1 lock抽象方法

```java

// 获取锁
abstract void lock();

```
### 1.2 nonfairTryAcquire方法

获取不公平锁。 用到`getState();`。如果为0，则CAS方法获得，并设置`setExclusiveOwnerThread`当前使用的进程为当前进程。如果当前没有获得锁并且锁的资源不是0，就return false

    state: 等于0代表可直接获得的状态。>0表示被重入次数。

```java
/**
* Performs non-fair tryLock.  tryAcquire is implemented in
* subclasses, but both need nonfair try for trylock method.
*/
final boolean nonfairTryAcquire(int acquires) {
    final Thread current = Thread.currentThread();
    int c = getState();
    if (c == 0) { // 判断状态
        if (compareAndSetState(0, acquires)) { // 与公平锁就差在这里！！（公平锁有!hasQueuedPredecessors()&&）
            setExclusiveOwnerThread(current);
            return true;
        }
    }
    else if (current == getExclusiveOwnerThread()) { // 如果当前进程正在用锁，并且还继续申请了，则增加getState次数。
        int nextc = c + acquires;
        if (nextc < 0) // overflow
            throw new Error("Maximum lock count exceeded");
        setState(nextc);
        return true;
    }
    return false;
}
```

### 1.3 tryRelease

获得对象状态，尝试释放

```java
protected final boolean tryRelease(int releases) {
    int c = getState() - releases;
    if (Thread.currentThread() != getExclusiveOwnerThread())
        throw new IllegalMonitorStateException();
    boolean free = false;
    if (c == 0) {
        free = true;
        setExclusiveOwnerThread(null);
    }
    setState(c);
    return free;
}
```
## 2 NonfairSync源码

实现了Sync中的lock方法（非公平的方式）

非公平：因为nonfairTryAcquire中，每一次都尝试获得锁，并不会按照公平等待原则等待
```java
static final class NonfairSync extends Sync {
    private static final long serialVersionUID = 7316153563782823691L;

    /**
        * Performs lock.  Try immediate barge, backing up to normal
        * acquire on failure.
        */
    final void lock() {
        if (compareAndSetState(0, 1))
            setExclusiveOwnerThread(Thread.currentThread());
        else
            acquire(1);//AQS提供的acquire方法，首先调用`tryAcquire`获取资源，如果失败就将这个线程封装成Node添加在sync queue尾部添加结点，等待轮训。
    }

    protected final boolean tryAcquire(int acquires) {
        return nonfairTryAcquire(acquires); // Sync中的非公平的方式nonfairTryAcquire
    }
}
```

## 3 fairSync源码

实现了Sync中的lock方法（公平的方式）

```java
static final class FairSync extends Sync {
    private static final long serialVersionUID = -3000897897090466540L;

    final void lock() {
        acquire(1);
    }

    /**
        * Fair version of tryAcquire.  Don't grant access unless
        * recursive call or no waiters or is first.
        */
    protected final boolean tryAcquire(int acquires) {
        final Thread current = Thread.currentThread();
        int c = getState();
        if (c == 0) {
            if (!hasQueuedPredecessors() && // 与非公平锁就差在这里。判断是否有已经等待更久的线程
                compareAndSetState(0, acquires)) {
                setExclusiveOwnerThread(current);
                return true;
            }
        }
        else if (current == getExclusiveOwnerThread()) {
            int nextc = c + acquires;
            if (nextc < 0)
                throw new Error("Maximum lock count exceeded");
            setState(nextc);
            return true;
        }
        return false;
    }
}

```
**其中`!hasQueuedPredecessors() &&`判断是否有已经等待更久的线程, 用来实现公平锁**

- hasQueuedPredecessors：AQS中的方法

```java
    public final boolean hasQueuedPredecessors() {
        // The correctness of this depends on head being initialized
        // before tail and on head.next being accurate if the current
        // thread is first in queue.
        Node t = tail; // Read fields in reverse initialization order
        Node h = head;
        Node s;
        return h != t &&
            ((s = h.next) == null || s.thread != Thread.currentThread());
    }
```

因此ReentrantLock其实调用了AQS的acquire


# 构造函数

通过传入的参数决定公平还是非公平
```java
public ReentrantLock(boolean fair){
    sync = fair? new FairSync():new NonfairSync();
}
```