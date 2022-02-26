es# 实现方法
用的是堆来实现的priority queue，每次插入和删除都要使用上悬和下沉

堆使用一个数组实现的，因为是标准的二叉树

子节点index就是 2i and 2i+1

# 使用方法

priority_queue<>

`priority_queue<Type, Container, Functional>`
    
Type 就是数据类型，Container 就是容器类型（Container必须是用数组实现的容器，比如vector,deque等等，但不能用 list。STL里面默认用的是vector），Functional 就是比较的方式，
```

struct cmp{
    bool operator() (ListNode* l1, ListNode* l2){
        return l1->val<l2->val;
    }
};
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