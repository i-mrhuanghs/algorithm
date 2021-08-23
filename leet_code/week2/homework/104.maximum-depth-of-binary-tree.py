#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
 # DFS
class Solution:
    # 确定递归函数的参数和返回值：参数就是传入树的根节点，返回就返回这棵树的深度，所以返回值为int类型。
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # 确定终止条件：如果为空节点的话，就返回0，表示高度为0。
        if root is None:
            return 0
        # 确定单层递归的逻辑：先求它的左子树的深度，再求的右子树的深度，最后取左右深度最大的数值 再+1 （加1是因为算上当前中间节点）就是目前节点为根节点的树的深度。
        leftDepth = self.maxDepth(root.left)
        rightDepth = self.maxDepth(root.right)
        depth = max(leftDepth,rightDepth)+1
        return depth
# @lc code=end

