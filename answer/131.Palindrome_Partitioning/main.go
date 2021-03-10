/*
深度优先搜索

图论：找两点之间所有路径

首先是一个基本的有向图，每个字符是一条边，任何两点之间如果是联通的，表示它们之间的字符构成回文。
先把所有的边计算出来。

然后找起始点到终点的所有路径。

 */


package main

import "fmt"

func partition(s string) [][]string {
	var r [][]string
	var is_palindrome [16][16]bool // is_is_palindrome[i][j] = True means s[i:j]
	var i, j , size int

	for i = 0; i < len(s); i ++ {
		is_palindrome[i][i] = true
	}
	for i = 1; i < len(s); i ++ {
		j = i - 1
		if s[i] == s[j]{
			is_palindrome[i][j] = true
		}
	}
	for size = 3; size < len(s); size ++ {
		for i = 0; i + size - 1 < len(s); i ++ {
			j = i + size - 1
			if is_palindrome[i+1][j-1] {
				if s[i] == s[j] {
					is_palindrome[i][j] = true
				}
			}
		}
	}






	return r
}


func main() {
	var s = "afasdfa"
	fmt.Println(len(s))
	fmt.Println("hello world!")
	partition(s)
}



