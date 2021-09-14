#
# @lc app=leetcode id=64 lang=python3
#
# [64] Minimum Path Sum
#
from typing import List
# @lc code=start
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]: return 0
        rows, columns = len(grid), len(grid[0])
        dp = [[0] * columns for _ in range(rows)]
        dp[0][0] = grid[0][0]
        for i in range(1, rows):
            dp[i][0] = dp[i-1][0] + grid[i][0]
        for j in range(1, columns):
            dp[0][j] = dp[0][j-1] + grid[0][j]
        for i in range(1, rows):
            for j in range(1, columns):
                dp[i][j] = min(dp[i-1][j],dp[i][j-1]) + grid[i][j]
        return dp[rows - 1][columns - 1]
# @lc code=end
"""
# 动态规划
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]: # 处理为空的特殊情况
            return 0
        
        rows, columns = len(grid), len(grid[0]) # 列，行
        dp = [[0] * columns for _ in range(rows)] # dp列表初始化
        dp[0][0] = grid[0][0] # 左上角点 dp
        for i in range(1, rows): # 处理第一列的dp
            dp[i][0] = dp[i - 1][0] + grid[i][0]
        for j in range(1, columns): # 处理第一行的dp
            dp[0][j] = dp[0][j - 1] + grid[0][j]
        for i in range(1, rows): # 处理其他行列 每个点的dp 是上 或 左点的dp +该点的值
            for j in range(1, columns):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
        
        return dp[rows - 1][columns - 1]
"""
