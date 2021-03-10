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

# 队列

队列本质上也是一个表，只是Insert和Delete分别只能在表的两端。


# 树（二叉树，AVL树，B树）

遍历方法

# 散列

# 堆

# 排序

# 不相交集ADT

# 图论

- 拓扑排序
- 最短路径

# 深度优先搜索

```


```

