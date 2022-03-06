# 堆

首先堆排序就是先构建堆，然后每次取出堆首元素即可。

适用场景：
- 堆排序：元素非常多时，可以直接维护一个比较小的固定长度的堆。
- 优先队列


## 堆的构建、插入与删除

数组组成
```cpp
void downAdjust(int low, int down) {
    int child = low * 2;
    while (child < down) {
        if (heap[child] < heap[child + 1]) {
            child++;
        }
        if (heap[child] > heap[low]) {
            swap(low, child);
            low = child;
        } else {
            break;
        }
    }
}
void createHeap() {
    int n = heap.size();
    for (int i = n / 2; i > 0; i--) {
        downAdjust(i, n);
    }
}

```

堆的插入与删除
```cpp
void insertHeap(int num) {
    // 插入节点后，只用从下往上遍历
    heap.push_back(num);
    upAdjust(heap.size() - 1);
}

void upAdjust(int index) {
    while (index != 1) {
        int parent = index/2;
        if(heap[index] <= heap[parent]) {
            break;
        }
        swap(index, parent);
        index = index/2;
    }
}

void deleteNum(int num) {
    // find index in vector
    // swap(index, last_node)
    // downAdjust(index, n-1)
}
```

## 优先队列