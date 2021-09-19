# ES

分布式的，提供实时的搜索和分析引擎。把所有操作封装成了http的api`curl -XPUT 'http://ip:port/poems'`

利用分片实现分布式。相当于水平分表，将一个索引中的数据保存在多个分片中。分片又被分配到集群的各个节点Node。ES会自动在Node中迁移分片，从而实现集群规模的扩展等。

master-slave框架。节点对等，选择集群的master, master负责集群信息的改变与同步。
只有建立索引和类型通知master, 其他的读写可以rout到集群的任意节点。

方式：爬取内容-》进行分词-》建立方向索引。

![es](./pic/es.jpeg)

## 存储简单模式：
store entire objects or document。document有多个fields, 为这些fields创建倒排索引并一起存入。

每一个document都保存在多个分片（Shard）中。但是应用程序与index交互而不是分片。

## 一些关键词
- 索引index：放数据的地方，类似于mysql的数据库（全小写）
- 类型type：索引内部逻辑分区。类似mysql中的一张表，内部的逻辑分区，根据需求来讲,例如一个存储用户数据结构，一个存储评论数据的类型。
- 文档：基于Json格式表示。最终的数据。（把数据组织成json格式放进去），针对JSON文档中每一个field都会建立一个对应的倒排索引。

## Lucene存储的数据结构

分成两个部分：字典和倒排表。字典是term的集合。字典中的term指向一个文档链表的集合。是分两部分存储的。倒排表不仅存储了文档编号，还有词频等信息。


## Java API
- Node client
- Transport client
![trans](./pic/trans.jpeg)
## ES底层写操作

1. create: 用户向某个node提交索引新文档的请求）。node计算document属于哪个shard分片。每个节点都知道shard在哪个node中。因此协调节点将请求发送给该node。

        1.1: node中的主分片收到请求完成索引。
        1.2: 这个请求并行发送给其他副本分片维持更新

2. refresh: 定时将数据写到磁盘。定时写到文件系统缓存，构成segment。30min将segment写入磁盘。translog被删除（translog用来记录两次吸写入数据之间的操作，防止断电丢失）

3. delete：索引不能被删除，只能在del文件中记录，删除时自动过滤。更新维护一个版本号。

## ES底层查询方法

1. 节点收到一个search请求，节点变成协调节点
2. 广播到每个索引中的每个节点的分片，查询是否可以被处理。
3. 分片维护一个优先级队列（因为是排好顺序的）
4. 最后协调节点将所有分片的结果汇总。全局排序

## ES的使用方法

> 要存储一个员工信息表，包含多种信息
### 存储

1. indexing exployee Document: 一个document代表一个employee。（包括id）
2. document的type为exployee
3. type放到某个名字为m_index的index里。
4. 索引放到ES集群中。
``` sql
PUT /m_index/exployee/1（id）
{
    "firstname":"Json",
    "interests":"[1,2]"
}
```
### seach

#### 1. 通过document id:
 `GET /m_index/exployee/1`, 得到的信息就在_source中

#### 2. 通过_search query：

##### 2.1 url写法
`GET /m_index/employee/_search?q=last_name:Smith`, 得到结果在“hits”中

##### 2.2 json写法

1.  match
```sql
GET /m_index/employee/_search
{
    "query":{
        "match":{
            "last_name":"Smitch"
        }
    }
}

```
2.  复杂化搜索
例如运用bool进行和判断or或判断等

3.  全文搜索
**full-text search**（优点）

例如json中about字段存储的是一大段话。但是想搜索这一大段话中的某个词组。则只需要搜索一下代码即可。
返回的结果是出现rock or climbing的所有结果。结果按照排序程度排序并返回。例如出现rock climbing比只出现rock的分数高。

```sql
GET /m_index/employee/_search
{
    "query":{
        "match":{ 
            "about":"rock climbing"
        }
    }
}

```
> match换成match_phase就能支持精准短语搜索。

