#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        newListNode = ListNode()
        tempListNode = newListNode
        while l1 and l2:
            if l1.val < l2.val:
                tempListNode.next = l1
                l1 = l1.next
            else:
                tempListNode.next = l2
                l2 = l2.next
            tempListNode = tempListNode.next
        tempListNode.next = l1 if l1 is not None else l2
        return newListNode.next
# @lc code=end
