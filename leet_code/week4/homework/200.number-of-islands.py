#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#

# @lc code=start
from typing import List
class Solution:
    def dfs(self, grid: List[List[str]], r:int, c: int) -> None:
        grid[r][c] = 0
        for x, y in ((r+1, c),(r-1, c), (r, c-1), (r, c+1)):
            if x<=len(grid) and y<=len(grid[0]) and grid[x][y] == "1":
                self.dfs(grid, x, y)

    def numIslands(self, grid: List[List[str]]) -> int:
        nr = len(grid)
        if nr == 0: return 0
        nc = len(grid[0])
        num_islands = 0
        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == "1":
                    num_islands += 1
                    self.dfs(grid, r, c)
        return num_islands


# @lc code=end
"""
from typing import List
class Solution:
    def dfs(self, grid, r, c):
        grid[r][c] = 0 # 把该值变为0
        nr, nc = len(grid), len(grid[0]) # 遇到在边界范围内的“1”，把它附近的点都递归感染成“0”
        for x, y in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
            if 0 <= x < nr and 0 <= y < nc and grid[x][y] == "1":
                self.dfs(grid, x, y)

    def numIslands(self, grid: List[List[str]]) -> int:
        nr = len(grid) # 长
        if nr == 0: # 特殊情况判断
            return 0
        nc = len(grid[0]) # 宽

        num_islands = 0
        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == "1": # 遇见“1” 岛屿数量加一 并递归把这个点附近的值都感染成0
                    num_islands += 1
                    self.dfs(grid, r, c)
        
        return num_islands
"""
