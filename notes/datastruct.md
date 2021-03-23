# 最大子序列和问题（子序列是连续的）

给定整数A[1], A[2], ..., A[N]，可能有负数， 求Sum A[i..j] 的最大值。

```
int MaxSubsequenceSum( const int A[], int N) {

    int ThisSum, MaxSum, j;

    ThisSum = MaxSum = 0;
    for ( j = 0; j < N; j ++){
        ThisSum += A[j];

        if (ThisSum > MaxSum) {
            MaxSum = ThisSum
        }else if (ThisSum < 0 ){
            ThisSum = 0
        }
    }

    return MaxSum;
}

```





# 表

A[1], A[2], A[3], ... , A[N] 就是一个大小为N的表。

## ADT接口

- Insert
- Delete
- FindKth

实现方式有数组和链表两种方式。

数组的Insert和Delete需要移动其它元素，但是FindKth是O（1），链表则相反。


常见题目：

输入一个整数数列，返回第K大的元素。(排序的问题）。

选课问题：

40000名学生和2500门课程。列出每个班的注册者；列出每个学生注册的班级。用二维链表存储信息。



# 栈

栈本质上也是一个表，只是Insert和Delete只能在表的顶端。

## ADT接口

- POP
- PUSH

常见题目：

- 大中小括号匹配（编译器领域的应用）
- 后缀表达式（逆波兰记法）：遇到操作数进栈，遇到运算符，从栈中取出两个操作数，计算，然后进栈。
- 中缀表达式转后缀表达式：遇到操作数，输出，遇到运算符，和栈顶的运算符比较优先级。遇到括号，也要进栈。


### 最小栈

每次Push一个键值对，一个保存正常值，一个保存最小值。



# 队列

队列本质上也是一个表，只是Insert和Delete分别只能在表的两端。


# 树（二叉树，AVL树，B树）

遍历方法

# 散列

# 堆

# 排序

### 冒泡排序

```
//冒泡排序 比较两个相邻元素，大的放后面
//每一轮都会把该轮最大值的放后面
void pop_sort(int arr[], int len) {
    int temp;
    //len-1的原因是  两个元素只需要排一趟，len个元素只需len-1趟
    for (int i = 0; i < len-1; i++) {
        for (int j = 0; j < len-i-1; j++) {
            if (arr[j] > arr[j+1]) {
                temp = arr[j + 1];
                arr[j + 1] = arr[j];
                arr[j] = temp;
            }
        }
    }
}
```

### 选择排序

```
//选择排序，每次在未排序的元素中找到最大值/最小值放到末尾/开头
//只需将最小/大的元素和末尾/开头元素调换位置

//最小
void chose_sort1(int arr[], int len) {
    int min;
    for (int i = 0; i < len - 1; i++) {
        min = i;
        for (int j = i+1; j < len; j++) {
            if (arr[j] < arr[min]) {
                min = j;
            }
        }
        int temp;
        temp = arr[i];
        arr[i] = arr[min];
        arr[min] = temp;
    }
}

//最大
void chose_sort2(int arr[], int len) {
    int max;
    for (int i = 0; i < len - 1; i++) {
        max = len-i-1;
        for (int j = 0; j < len-i-1; j++) {
            if (arr[j] >arr[max]) {
                max = j;
            }
        }
        int temp;
        temp = arr[len-i-1];
        arr[len-i-1] = arr[max];
        arr[max] = temp;
    }
}

```

### 插入排序

```
//插len-1趟，初始化，第一个元素当初被排序过的序列，
//从头到尾扫描没被排序的序列，将其插入到排序的序列中,
//特别注意尾部开始插入 头插的话太麻烦
void insert_sort(int arr[], int len) {
    //i表示当前要插入的元素，从第二个元素开始
    for (int i = 1; i < len; i++) {
        int key = arr[i];//要插入的元素
        int j = i - 1;//j表示已排序序列的最后一位
        while (j >= 0 &&key<arr[j]) {
            arr[j + 1] = arr[j];
            j--;
        }
        arr[j+1] = key;

    }
}

```

### 快速排序

```

void quick_sort(int arr[], int left, int right)
{
    int i,j,t,temp;

    if(left>right)
        return;

    temp = arr[left];
    i = left;
    j = right;

    while(i != j)
    {
        while(i<j && arr[j]>=temp)
            j--;
        while(i<j && arr[i]<=temp)
            i++;

        if(i < j)
        {
            t = arr[i];
            arr[i] = arr[j];
            arr[j] = t;
        }
    }

    arr[left] = arr[i];
    arr[i] = temp;

    quick_sort(arr, left, i-1);
    quick_sort(arr, j+1, right);
}

```

# 不相交集ADT

# 图论

- 拓扑排序
- 最短路径

# 深度优先搜索

```


```

# 动态规划

#### [字符串匹配 正则表达式匹配](https://www.nowcoder.com/practice/43072d50a6eb44d2a6c816a283b02036)

dp[i][j] ——表示 s 的前 i 个字符和 p 的前 j 个是否匹配；



