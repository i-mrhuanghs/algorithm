#
# @lc app=leetcode id=547 lang=python3
#
# [547] Number of Provinces
#
from typing import List
# @lc code=start
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(i: int):
            for j in range(provinces):
                if isConnected[i][j] == 1 and j not in visited:
                    visited.add(j)
                    dfs(j)
        provinces = len(isConnected)
        visited = set()
        circles = 0

        for i in range(provinces):
            if i not in visited:
                dfs(i)
                circles += 1
        
        return circles
# @lc code=end

