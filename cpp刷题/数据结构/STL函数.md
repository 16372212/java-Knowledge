vector<int> pre;
# lower_bound
lower_bound( begin,end,num)：从数组的begin位置到end-1位置二分查找第一个大于或等于num的数字，找到返回该数字的地址，不存在则返回end。通过返回的地址减去起始地址begin,得到找到数字在数组中的下标。
`lower_bound(pre.begin(), pre.end(), x)`

头文件：
```
#include <algorithm>    std::lower_bound, std::upper_bound, std::sort
```
# upper_bound
upper_bound( begin,end,num)：从数组的begin位置到end-1位置二分查找第一个大于num的数字，找到返回该数字的地址，不存在则返回end。通过返回的地址减去起始地址begin,得到找到数字在数组中的下标


# accumulate
accumulate定义在#include<numeric>中，作用有两个，一个是累加求和，另一个是自定义类型数据的处理
`int sum = accumulate(vec.begin() , vec.end() , 42); `
三个参数：起始vector，终止vector，和的起始
对于String类型的元素，可以将起始元素设置为“ tempstr”都可以

