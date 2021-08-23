#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self) -> None:
        self.pre = float('-inf')
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root: return True
        if not self.isValidBST(root.left): return False
        if self.pre >= root.val: return False
        self.pre = root.val
        return self.isValidBST(root.right)
# @lc code=end

