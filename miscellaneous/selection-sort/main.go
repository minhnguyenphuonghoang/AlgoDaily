package main

import "fmt"

/*
	Selection Sort:
	- The selection sort algorithm sorts an array by repeatedly finding the minimum element
		(considering ascending order) from unsorted part and putting it at the beginning
	- in-place
*/
func selectionSort(nums []int) {
	for i := 0; i < len(nums); i++ {
		min_idx := i
		for j := i; j < len(nums); j++ {
			if nums[j] < nums[min_idx] {
				min_idx = j
			}
		}
		temp := nums[i]
		nums[i] = nums[min_idx]
		nums[min_idx] = temp
	}
}

func main() {
	a := []int{64, 25, 12, 22, 11}
	selectionSort(a)
	fmt.Println(a)
}