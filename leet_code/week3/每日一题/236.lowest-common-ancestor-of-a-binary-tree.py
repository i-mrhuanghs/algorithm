#
# @lc app=leetcode id=236 lang=python3
#
# [236] Lowest Common Ancestor of a Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        parent = dict()
        visted = set()
        # 递归遍历树的所有的节点 并记录每个节点的父节点
        def dfs(root: 'TreeNode') -> None:
            if root.left != None:
                parent[root.left.val] = root
                dfs(root.left)
            if root.right != None:
                parent[root.right.val] = root
                dfs(root.right)
        dfs(root)
        # 先把一个节点从下往上，把它的所有父节点记录下来
        while p:
            visted.add(p.val)
            p = parent.get(p.val)
        # 再访问另一个节点从小往上， 找到第一个共同的父节点
        while q:
            if q.val in visted:
                return q
            q = parent.get(q.val)
        # 处理空值的情况
        return root
# @lc code=end
"""
# 递归 找左右子树的是否含有根节点
class Solution:
    def __init__(self) -> None:
        self.ans = None
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> None:
            # 终止条件
            if not root: return
            # 进入下一层
            lson = dfs(root.left, p, q)
            rson = dfs(root.right, p, q)
            # 这层的处理逻辑 如果两个节点分别在左子树的左子树和右子树 ｜ 一个是根结点 另一个在左或右子树上 
            if (lson and rson) or ((root.val==p.val or root.val==q.val) and (lson or rson)):
                self.ans = root
            # 判断两个节点是否在左右子树中 或者说是在根节点中 为最终结果服务
            return lson or rson or root.val==p.val or root.val==q.val
        dfs(root, p, q)
        return self.ans



# 存储父节点
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        parent = dict()
        visted = set()
        # 递归遍历树的所有的节点 并记录每个节点的父节点
        def dfs(root: 'TreeNode') -> None:
            if root.left != None:
                parent[root.left.val] = root
                dfs(root.left)
            if root.right != None:
                parent[root.right.val] = root
                dfs(root.right)
        dfs(root)
        # 先把一个节点从下往上，把它的所有父节点记录下来
        while p:
            visted.add(p.val)
            p = parent.get(p.val)
        # 再访问另一个节点从小往上， 找到第一个共同的父节点
        while q:
            if q.val in visted:
                return q
            q = parent.get(q.val)
        # 处理空值的情况
        return root
"""
