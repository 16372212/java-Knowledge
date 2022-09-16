# 微软aa
项目相关

## 1 我的项目

### 总结

负责ASA与Spark Streaming的性能对比。构建多种数据集，并针对多种数据集来衡量这两种大数据处理工具在同等环境下消费性能的区别。

分别从两个维度来测试两个指标：

1. 相同硬件配置：node（executor）个数、输入流式数据吞吐。或者相同开销（databrick下用的标准节点还是普通节点，）
**2. Databrick怎么实现的高可用？**

得到的结论：在Memory使用上，和Spark差了一倍。例如Join Spark最大的window是17min，而Join ASA是9min.
CPU上，对于基本的Select and UDF, 性能ASA略差于Spark。但是改进后好了很多，提升了一倍。


> 为什么后来Window越大，吞吐就越小的？

> 怎么才算得到最大的Window的：ASA这里不停的发生oom 的exeception。Databrick发现了node节点被打挂了然后重启的现象。


### 1. 配置与工具选择


> why use blob, not datalake?

Azure Blob 存储是一个常规用途和可扩展的对象存储，适用于多种存储方案。 Azure Data Lake Storage Gen1 是一个针对大数据分析工作负荷进行了优化的超大规模存储库。

Azure Data Lake:
*文件系统*， 适用于大数据分析工作负载。
Data Lake Storage Gen1 是一个 Apache Hadoop 文件系统，和Haddoop的分布式文件系统 (HDFS) 兼容并与 Hadoop 生态系统相互协作。

它对帐户大小、文件大小或 Data Lake 中可存储的数据量、存储时间均无任何限制。 

Blob是*对象存储*工具。



node、executor、worker、
倍压策略
乱序有序对于watermark delay的影响

### 技术难点

### 测试步骤

调整的参数有那些、策略等等

### 未来改进，怎么优化


## 2 ASA



## 3 Spark

Spark相关基本技术





## Databrick

自动化集群管理。

1. 硬件配置：定义的时候用的什么单位：,databrick的memory配置等等

Cluster Mode：集群的模式共有三种，High concurrency（高并发）、Standard（标准）和Single Node（单节点）。标准模式是推荐模式，通常用于单用户的集群

Runtime

2. 怎么实现的HA高可用，在only one driver and one worker,
3. 用的什么配置：Spark支持三种环境。databrick帮它实现的哪一种？

Spark分布式架构与单机多核架构的异同，Databrick用的是哪一个，我选择的是哪一个？

应用场景：

在分布式运算下，数据尽量本地运算，减少网络I/O开销。由于大规模分布式系统要在不同处理单元之间传送信息，在网络传输少时，系统可以充分发挥资源的优势，达到高效率。

### 做什么的
Databrick可以作为
1. SQL
2. 数据科学：基于Spark的数据分析平台。和Azure集成
3. 机器学习

Azure Databricks 通过 I/O 层和处理层 (Databricks I/O) 的各种优化提供了一个更快速、更高效的 Spark 引擎。

### 用了databrick哪些功能

#### 1. 创建集群
#### 2. 创建笔记本
#### 3. 配置*自动加载程序*以将数据引入 Delta Lake

a. 自动加载程序：

（而不是结构化流，例如spark.readStream.format()这种）
> 从提供的云文件的存储路径自动加载云文件。cloudFiles（结构化流式处理源）源将在新文件到达时自动处理这些文件。

优势：

1. 自动加载程序可缩放以支持每小时近实时引入数百万个文件。
2. 只处理一次数据：元数据都会被保存在自动加载程序管道的检查点CheckPoint位置的RockDB(可缩放键值存储)中。
3. 容错：根据存储在检查点位置的信息从中断的位置恢复，并在将数据写入 Delta Lake 时继续提供一次性保证。
4. 优化：可以根据数据量、多样性和速度来优化自动加载程序
5. 

b. Delta lake
## 其他项目

代码如何变成jar包

项目的框架，上游下游

用了那些参数，公式是什么

整体的流程和步骤

## 可能的问题：

1. 使用AWS，GCS上传文件时，如何保证中间传输错误后，仍然是一次性读取。且有容错机制？
