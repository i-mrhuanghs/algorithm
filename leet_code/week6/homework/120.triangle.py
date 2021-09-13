#
# @lc app=leetcode id=120 lang=python3
#
# [120] Triangle
#
from typing import List
# @lc code=start
# 从下往上 不需要排序
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = triangle[-1] # 从底向上
        for i in range(len(triangle)-2,-1,-1): # 从低向上遍历未取的行
            for j in range(0,i+1): # 把每一行一点的都从下面的行的中j+1,j中取一个最小值并和该点的权值做和
                dp[j] = min(dp[j], dp[j+1]) + triangle[i][j]
        return dp[0] # 从低向上 dp[0]就是最小的路径值了
# @lc code=end
"""
# 从上往下
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle) # n的长度
        f = [[0] * n for _ in range(n)] # n行n列列表 记录到达每个点最短的距离
        f[0][0] = triangle[0][0] # 第一行单独处理

        for i in range(1, n): # 遍历每行
            f[i][0] = f[i - 1][0] + triangle[i][0] # 单独处理最左边的点到达的最短距离 是上一行0能到达该点
            for j in range(1, i):
                f[i][j] = min(f[i - 1][j - 1], f[i - 1][j]) + triangle[i][j] # 一点的距离是上行的点j-1，j的最短距离+该点的权
            f[i][i] = f[i - 1][i - 1] + triangle[i][i]# 单独处理最右边的点到达的最短距离，只有上一行i-1能到达该点
        
        return min(f[n - 1])
#变量名认真版
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        tri_len = len(triangle)
        dp = [[0] * tri_len for _ in range(tri_len)]
        dp[0][0] = triangle[0][0]
        for i in range(1,tri_len):
            dp[i][0] = dp[i-1][0] + triangle[i][0]
            for j in range(1,i):
                dp[i][j] = min(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]
            dp[i][i] = dp[i-1][i-1] + triangle[i][i]
        return min(dp[tri_len-1])

# 空间优化 两个列表
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        tri_len = len(triangle)
        dp = [[0] * tri_len for _ in range(2)]
        dp[0][0] = triangle[0][0]
        for i in range(1,tri_len):
            curr, prev  = i % 2, 1 - i % 2 # 交替使用两个数组的关键
            dp[curr][0] = dp[prev][0] + triangle[i][0]
            for j in range(1,i):
                dp[curr][j] = min(dp[prev][j-1], dp[prev][j]) + triangle[i][j]
            dp[curr][i] = dp[prev][i-1] + triangle[i][i]
        return min(dp[curr])

# 空间优化 一个列表
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        tri_len = len(triangle)
        dp = [0] * tri_len
        dp[0] = triangle[0][0]
        for i in range(1,tri_len):
            dp[i] = dp[i-1] + triangle[i][i]
            for j in range(i-1,0,-1):
                dp[j] = min(dp[j-1], dp[j]) + triangle[i][j]
            dp[0] = dp[0] + triangle[i][0]
        return min(dp)

# 从下往上 不需要排序
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = triangle[-1] # 从底向上
        for i in range(len(triangle)-2,-1,-1): # 从低向上遍历未取的行
            for j in range(0,i+1): # 把每一行一点的都从下面的行的中j+1,j中取一个最小值并和该点的权值做和
                dp[j] = min(dp[j], dp[j+1]) + triangle[i][j]
        return dp[0] # 从低向上 dp[0]就是最小的路径值了
"""
