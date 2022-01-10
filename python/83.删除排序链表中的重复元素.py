#
# @lc app=leetcode.cn id=83 lang=python3
#
# [83] 删除排序链表中的重复元素
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:

        thisNode = head
        while thisNode != None and thisNode.next != None:
            if thisNode.next.val == thisNode.val:
                thisNode.next = thisNode.next.next
            else:
                thisNode = thisNode.next
        return head

# @lc code=end

