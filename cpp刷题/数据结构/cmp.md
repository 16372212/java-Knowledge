c++倒序排列

1 比较函数

cmp函数倒序排列：sort(vector.begin(), vector.end(), cmp)
// int型
bool cmp(int a, int b){
return a>b;
}

// string型
bool cmp(const Student& lhs, const Student& rhs){
return lhs.grade < rhs.grade
|| (lhs.grade == rhs.grade && lhs.name < rhs.name);
}
2 改变顺序（如果不是正序，那么reverse后也不是正确顺序）reverse(,)