## java加锁的方法

    synchronized关键字和Lock的实现类都是悲观锁

    乐观锁：CAS算法compare and swap

- 需要读写的内存值 V。
- 进行比较的值 A。
- 要写入的新值 B。
- 当且仅当 V 的值等于 A 时，CAS通过原子方式用新值B来更新V的值（“比较+更新”整体是一个原子操作）

```java
// ------------------------- 悲观锁的调用方式 -------------------------
// synchronized
public synchronized void testMethod() {
	// 操作同步资源
}
// ReentrantLock
private ReentrantLock lock = new ReentrantLock(); // 需要保证多个线程使用的是同一个锁
public void modifyPublicResources() {
	lock.lock();
	// 操作同步资源
	lock.unlock();
}

// ------------------------- 乐观锁的调用方式 -------------------------
private AtomicInteger atomicInteger = new AtomicInteger();  // 需要保证多个线程使用的是同一个AtomicInteger
atomicInteger.incrementAndGet(); //执行自增1

```

### synchronized 和lock的区别？

synchronized是关键字，（cpu悲观锁实现，上下文切换）锁的释放有两种：线程执行完或者线程发生异常。synchronized必须是非公平锁

lock是一个接口，里面有实现锁的一些方法。锁的释放必须要finally中显示调用。例如lock（锁已被其他线程获取，则进行等待。）后必须由unlock()释放。

lock可以是公平锁也可能是非公平锁。例如，ReentrantLock是通过AQS的来实现线程调度。

## java写一个生产者和消费者

```java
public class Concurrentcomm {
    //常量
    private static int MAX_VALUE = 10;
    //可以理解为缓存
    LinkedList<String> linkedList = new LinkedList<>();
    // Object object = new Object();

    public void product() throws Exception{
        synchronized(linkedList){
            while(MAX_VALUE.equals(linkedList.size())){
                linkedList.wait();
                // 此时已满
            }
            linkedList.push("lisi");
            System.out.println("lisi 生产了一个瓜");
            linkedList.notifyAll(); // 解除那些在该对象上调用wait()方法的线程的阻塞状态。该方法只能在同步方法或同步块内部调用。
        }
    }

    public void consumer() throws Exception{
        synchronized(linkedList){
            while(MAX_VALUE.equals(0)){
                linkedList.wait();
                // 此时空的
            }
            linkedList.pop();
            System.out.println("lisi 消费了一个瓜");
            linkedList.notifyAll();
        }
    }
}

public class concurrent(){

    private static int MAX_VALUE = 100;

    public static void main(String[] args){
        Concurrentcomm comm = new Concurrentcomm();
        new Thread(new Runnable(){

            public void run(){
                try{
                    for (int i = 0; i < MAX_VALUE; i++) {
                        Thread.sleep(0);
                        comm.product();
                    }
                }catch(Exception e){
                    e.printStackTrace();
                }
            }

        }).start();

        new Thread(new Runnable{
            public void run(){
                try{
                    for (int i = 0; i < MAX_VALUE; i++) {
                        comm.consumer();
                    }
                }catch(Exception e){
                    e.printStackTrace();
                }
            }
        }).start();
    }
}

```

## 奇偶加锁

```java
// 使用synchronized结合wait, notify实现
public class PrintOddEven{

    private static int count = 0;
    private static final Object object = new Object();

    public static void main(String[] args){
        new Thread(new printer(), "奇数线程").start();
        new Thread(new printer(), "偶数线程").start();
    }

    static class printer implements Runnable{
        public Runnable(){
            while(count <= 100){
                synchronized(object){
                    System.out.println(Thread.currentThread().getName() + "打印:" + count++);
                    object.notify();
                    if(count <= 100){
                        try{
                            object.wait();
                        }catch (InterruptedException e) {
                            e.printStackTrace();
                        }
                    }
                }
            }
        }
    }
}

```

## 徒手写java创建进程的代码，下次尝试写一些sql语句

## 微博按照关注的人时间倒序

SELECT id, name FROM user WHERE 

## ThreadLocal

解决线程安全问题，每个线程提供一个独立的变量。
将某个类变量放到threadlocal类型的对象中，每个线程都有自己对这个变量的副本。线程读取变量不用担心被别的变量改变。

synchronized: 同一时刻只有一个线程对共享变量进行操作

## 一亿个数里判断是否出现某个数

## Linux 如何查询进程占用，top 和ps， top的参数有哪些？

## 

