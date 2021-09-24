# IO

> 套接字： 1 等待数据从网络中到达，复制到内核某缓冲区。2 把数据从内核缓冲区复制到应用进程缓冲区。

![io](./pic/io.png)

## NIO

### 多路复用
![io](./pic/io多路复用.png)

### epoll, select, poll, ...

1. select

```java
            
int select(int maxfdp1, fd_set *readset, fd_set *writeset, fd_set *exceptset, const struct timeval * timeout)
// maxfdp1: 待测试的描述字个数
// readset，writeset, exceptest: 让内核测试读、写、异常条件的描述字。 
// timeout: 等待描述字花的时间
```


## reference


[1. 参考文章链接](https://www.pdai.tech/md/java/io/java-io-nio-select-epoll.html)

