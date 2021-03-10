/*

图论：找两点之间所有路径

首先是一个基本的有向图，每个字符是一条边，任何两点之间如果是联通的，表示它们之间的字符构成回文。
先把所有的边计算出来。

然后找起始点到终点的所有路径。

用深度优先搜索和广度优先搜索都可以，广度优先搜索需要申请


TODO: 怎么用非递归的写法

 */


package main

import "fmt"

func partition(s string) [][]string {
	var r [][]string
	var isPalindrome [17][17]int // is_palindrome[i][j] = True means s[i:j] is palindrome
	var i, j , size int
	var lastPoint = len(s)

	for i = 0; i < lastPoint; i ++ {
		isPalindrome[i][i+1] = 1
	}
	for i = 0; i < lastPoint-1; i ++ {
		if s[i] == s[i+1]{
			isPalindrome[i][i+2] = 1
		}
	}
	for size = 3; size <= lastPoint; size ++ {
		for i = 0; i + size <= lastPoint; i ++ {
			j = i + size

			if (isPalindrome[i+1][j-1] == 1 && s[i] == s[j-1]) {
				isPalindrome[i][j] = 1
			}
		}
	}


	var pathStack  = [17]int{0}


	var dfs func(int, int)

	dfs = func(top int, node int) {
		//fmt.Println(top, node)
		if node == lastPoint {
			splits := []string{}
			for stackIndex := 1; stackIndex < top + 1; stackIndex ++ {
				left := pathStack[stackIndex-1]
				right := pathStack[stackIndex]
				splits = append(splits, s[left:right])
			}
			r = append(r, splits)
			//fmt.Println(top, pathStack[:top+1], splits)
		}else{
			for toNode := node + 1; toNode <= lastPoint; toNode++{
				if isPalindrome[node][toNode] == 1 {
					pathStack[top + 1] = toNode
					dfs(top+1, toNode)
				}
			}
		}
	}

	dfs(0, 0)



	return r
}


func main() {
	var s = "aaaaaa"
	fmt.Println(len(s))
	fmt.Println("hello world!")
	partition(s)
	fmt.Println("finish")
}



