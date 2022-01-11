#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def _isSymmetric(self, left, right):
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False
        if left.val != right.val:
            return False
        if not self._isSymmetric(left.left, right.right):
            return False
        if not self._isSymmetric(left.right, right.left):
            return False
        return True

    def isSymmetric(self, root: TreeNode) -> bool:
        return self._isSymmetric(root.left, root.right)
        
# @lc code=end

