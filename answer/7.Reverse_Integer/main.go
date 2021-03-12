/*
整数转字符串
 */

package main

import "fmt"

func reverse(x int) int {
	var max_positive = []byte{}
	var max_negative = []byte{}

	var t = 2^31


	var int2c = map[int]string {1:"1",2:"2", 3:"3", 4:"4", 5:"5", 6:"6", 7:"7", 8:"8", 9:"0", ""}

	if x == 0 {
		return 0
	}

	var is_positive bool

	if x > 0{
		is_positive = true
	}else{
		is_positive = false
	}

	var splits = []int{}

	for x >= 10 || x <= -10 {
		splits = append(splits, x%10)
		x = x/10
	}
	splits = append(splits, x)

	fmt.Println(splits)
	return 0
}

func main(){
	fmt.Println(-321)
	fmt.Println(231)
	fmt.Println(0)
	fmt.Println(100)
}

