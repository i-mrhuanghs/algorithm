#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
from typing import Optional,List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root: return []
        res, stack = [], []
        while root or stack: # stack为空且root为null时，说明已经遍历结束
            while root: # 可以深入左子树
                stack.append(root)
                root = root.left
            root = stack.pop() # 否则访问栈中节点，并深入右子树
            res.append(root.val)
            root = root.right
        return res
# @lc code=end

"""
from typing import Optional,List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def dfs(root):
            if not root:
                return
            # 按照 左-打印-右的方式遍历	
            dfs(root.left)
            res.append(root.val)
            dfs(root.right)
        dfs(root)
        return res
递归实现

前序遍历：打印 - 左 - 右
中序遍历：左 - 打印 - 右
后序遍历：左 - 右 - 打印
题目要求的是中序遍历，那就按照 左-打印-右这种顺序遍历树就可以了，递归函数实现

终止条件：当前节点为空时
函数内：递归的调用左节点，打印当前节点，再递归调用右节点
时间复杂度：O(n)O(n)
空间复杂度：O(h)O(h)，h 是树的高度
"""
"""
from typing import Optional,List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        res, stack = [], []
        while root:
            if root.left: # 一直走到最左边
                stack.append(root)
                root = root.left
            else: # 到最左边的子树 中序遍历它
                while stack and not root.right: # 处理到头的节点
                    res.append(root.val)   
                    root = stack.pop()
                res.append(root.val) # 中
                root = root.right # 如果可以深入右子树，就继续深入右子树
        return res
常规解法
迭代 栈辅助解法
"""
"""
from typing import Optional,List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root: return []
        res, stack = [], []
        while root or stack: # stack为空且root为null时，说明已经遍历结束
            while root: # 可以深入左子树
                stack.append(root)
                root = root.left
            root = stack.pop() # 否则访问栈中节点，并深入右子树
            res.append(root.val)
            root = root.right
        return res
模版解法
迭代 栈辅助解法
边界条件

初始化 cur, stack, root
while stack或cur非空:
    while 循环：
        cur 向左下遍历
        cur的值入栈
        # 访问cur的值 （前序遍历）
    弹出节点 tmp
    # 访问tmp的值（中序遍历）
    # 对tmp判断：右节点为空或其子节点已经访问过
    cur回到tmp的右子树

"""