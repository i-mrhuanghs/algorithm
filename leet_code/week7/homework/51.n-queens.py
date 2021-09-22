#
# @lc app=leetcode id=51 lang=python3
#
# [51] N-Queens
#
from typing import List
# @lc code=start
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        sols = []
        def dfs(state, pd, nd):
            r = len(state)
            if r < n:
                for c in range(n):
                    if c not in state and c-r not in pd and c+r not in nd:
                        dfs(state+[c], pd|{c-r}, nd|{c+r})
            else: 
                sols.append(state)
        
        dfs([], set(), set())
        return [[f"{'.'*p}Q{'.'*(n-p-1)}" for p in sol] for sol in sols]
# @lc code=end

