# kafka
Kafka做什么的?

## kafka几个基础知识

1. Broker ［中间者，代理者]

Kafka集群包含多台服务器，一台Kafka服务器就是一个Broker，一个集群由多个broker组成，一个broker可以有多个topic。broker承担着中间缓存和分发的作用

2. Topic ［主题，类别，话题］
可以理解为是一种队列.用户信息类的消息的topic，我们定义为user-topic

3. producer
向Topic中发送消息的一方

4. consumer
向Topic中拉取／消费消息的一方

5. Replications［备份，复制］
分区的备份，以便容错，分布在其他broker上，每个broker上只能有0个或者1个replications

6. Consumer Group［消费者群组］
消费者群组，是有若干个消费者组成的集体，每个consumer属于一个特定的consumer group

7. Partition ［分区］
Kafka内在就是分布式的，一个broker中可以有多个topic，一个topic可以设置多个partition（分区）。每个partition在物理上对应一个文件夹，文件夹存储所有消息和索引文件。


    redis的LRU策略，保留热数据。或者mongo，使用mmap机制映射到内存里。

HTTPS的机制，加密的流程。

多线程安全怎么保证

    对于mysql，多线程查询时保证一个时间戳，保证安全

    redis: 对用一个key, 多个线程进行改写时，需要设置一个zookeeper实现分布式锁， zookeeper确保一个时间只有一个系统操作key. 别人不允许读写。

接触过 RPC 吗？（了解过，但没实际写过）
