## map 初始化
unordered map的写法：

unordered_map<string, int> m = {{"I", 1}, {"IV", 3}, {"IX", 8}, {"V", 5}, {"X", 10}, {"XL", 30}, {"XC", 80}, {"L", 50}, {"C", 100}, {"CD", 300}, {"CM", 800}, {"D", 500}, {"M", 1000}};
    如果key不存在，则m[key] 返回0

## unordered_map遍历key的方法

1. 便捷方法
```c++
for(auto& p: maps){
    p.first是key, p.second就是value
}
```
> unordered_map无法使用pair或者数组作为key

2. 规范方法
```c++

map<int, int>::iterator it = maps.find('b');
for( map<int, int>::iterator it = maps.begin(); it!= maps.end();it++){
    it->first; // key
    it->second;// value
}

// 删除元素：通过iterator, 或者通过key的值
```
## unordered_set遍历key的方法
1. 便捷方法
```c++
for(auto p: maps){
    p就是相应的值
}
```
2. 规范方法

```c++
set<int, int>::iterator it = sets.find('b');
for( set<int, int>::iterator it = sets.begin(); it!= sets.end();it++){
    int value = *it;
}
```
## 如何在遍历中删除元素
> 在遍历中直接erase删除元素会导致失败

1. 使用删除元素之前的迭代器定义下一个元素，
```c++
for(auto it = maps.begin(), it_next = it; it!=maps.end();it=it_next){
    it_next++;
    if(){
        maps.erase(it)
    }    
}
```

2. 
```c++
for(auto it=mymap.begin(); it!=mymap.end();) {
    if (it->first == target) {
        it = mymap.erase(it);   
    } else {
        it++;
    }
}
```
