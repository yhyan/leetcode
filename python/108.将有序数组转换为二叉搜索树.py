#
# @lc app=leetcode.cn id=108 lang=python3
#
# [108] 将有序数组转换为二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if len(nums) == 1:
            return TreeNode(nums[0], None, None)
        mid = int(len(nums)/2)
        # [0, mid - 1] mid [mid + 1, len(nums) - 1]
        left = None if mid - 1 < 0 else self.sortedArrayToBST(nums[0:mid])
        right = None if mid + 1 > len(nums) - 1 else self.sortedArrayToBST(nums[mid + 1:])
        return TreeNode(nums[mid], left, right)
        
# @lc code=end

