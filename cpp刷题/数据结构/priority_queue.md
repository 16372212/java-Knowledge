es# 实现方法
用的是堆来实现的priority queue，每次插入和删除都要使用上悬和下沉

堆使用一个数组实现的，因为是标准的二叉树

子节点index就是 2i and 2i+1

# 使用方法

priority_queue<>

`priority_queue<Type, Container, Functional>`


Type 就是数据类型，Container 就是容器类型（Container必须是用数组实现的容器，比如vector,deque等等，但不能用 list。**STL里面默认用的是vector**），Functional 就是比较的方式，

## 如果要用到小顶堆
则一般要把模板的3个参数都带进去。STL里面定义了一个仿函数greater<>，基本类型可以用这个仿函数声明小顶堆。

```c++
1. priority_queue<int> q;
2. priority_queue<int, vector<int>, greater<int> > q;
3. priority_queue<pair<int,int>,vector<pair<int,int> >,greater<pair<int,int> > > coll;



4. // 针对自定义, 默认用operator，所以这里只需要对operator进行一个改写就行了
bool operator<(Node a, Node b){
    if( a.x== b.x ) return a.y> b.y;
    return a.x> b.x;
}
priority_queue<Node> q;

// 同样也可以对operator>进行改写：
> 这里补充operator+运算符的基础知识：


5. // 或者这个
struct cmp{
    bool operator() ( Node a, Node b ){//默认是less函数
    //返回true时，a的优先级低于b的优先级（a排在b的后面）
        if( a.x== b.x ) return a.y> b.y;      
        return a.x> b.x; 
    }
};
priority_queue<Node, vector<Node>, cmp> q;

```

# func

```
top 访问队头元素
empty 队列是否为空
size 返回队列内元素个数
push 插入元素到队尾 (并排序)
emplace 原地构造一个元素并插入队列
pop 弹出队头元素
swap 交换内容

```

复杂度，（大致有序的时候是O(logn)）
# 注意事项
因为是一个queue结构，所以要考虑到cmp>号出来的，顶是最小值


# cmp的写法和sort函数需要的写法不同
sort的cmp:
```c++
static bool cmp(int a , int b){
       return a<b;
}
```
而有的时候会报错：
写在类内时，cmp函数需要是静态函数，要加上static。