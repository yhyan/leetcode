/*

1. 暴力破解法 O(N^2)
2. 排序，二分查找 O(NlgN)
3. 本质上是需要查找一个数是否存在，可以先用hash表存储。Python里面的set，Golang中的map

 */

package main

import "fmt"

func twoSum(nums []int, target int) []int {
	var intTable = map[int]int{}
	var other int

	for i:=0; i < len(nums); i++{
		intTable[nums[i]] = i
	}
	for i:=0; i < len(nums); i++{
		other = target - nums[i]
		val, ok := intTable[other]
		if ok && val != i{
			return []int{i, val}
		}
	}
	return []int{}
}


func main(){
	var r = twoSum([]int{2,7,11,15}, 9)
	fmt.Println(r)

}
