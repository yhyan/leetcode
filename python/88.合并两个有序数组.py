#
# @lc app=leetcode.cn id=88 lang=python3
#
# [88] 合并两个有序数组
#

# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(n):
            nums1.pop()
        i = 0
        pos = 0
        while i < len(nums2):
            x = nums2[i]

            if pos >= len(nums1):
                nums1.append(x)
                pos += 1
                i += 1
            elif nums1[pos] < x:
                pos += 1
            else:
                # now nums1[pos] >= x
                nums1.insert(pos, x)
                # pos += 1
                i += 1


        

# @lc code=end

