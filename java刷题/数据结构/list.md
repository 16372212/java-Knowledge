# 初始化

```java
public class List {
    int getLen(int[] list) {
        if (list == null) {
            return 0;
        }
        return list.length;
    }
    void sortList(String[] str) {
        for (String i : str) { // 这么循环很好
            System.out.println(i);
        }
        int len = getLen(str);
    }
    int getLen(String[] str){
        return str.length;
    }
    public static void main(String[] args) {
        // 数组一旦创建后，大小就不可变.
        int[] list1 = new int[5];
        int[] list2 = new int[]{1, 2, 3};
        int[] list3 = {1, 2, 3};
        System.out.println("hello list");

        String[] str = new String[]{"abc", "efg"};
        String first = str[0];
        str[0] = "kkk";
        System.out.println(first); // abc
        /*
        sortList(str);
        直接这么声明方法会warn: Non-static method cannot be referenced from a static context
        解决方法一：在调用Main class内部的函数没有实例化，因此，需要把Main obj=new Main(); 添上，并且用obj.appleShare(m,n)。
        解决方法二：把appleShare函数改成static 函数。 即：pubic static int appleShare(m,n){.........}

        但是其他非main的函数就可以调用这个函数！
        */
    }
}
```