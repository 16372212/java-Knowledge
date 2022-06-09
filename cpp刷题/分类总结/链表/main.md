# 合并K个升序链表

1. 循环方式遍历链表：

很容易出错的一个点：
```cpp
for(auto list: lists){
    // 在循环中没办法对这个指针进行修改。所以需要将这里的list改成 &list
    // for(auto &list: lists){ 改成这样！
    list = list->next;
}
```