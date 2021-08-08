# @before-stub-for-debug-begin
from python3problem70 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [1,1]
        if n <= 1:
            return dp[n]
        for i in range(2,n+1):
            dp.append(dp[i-1]+dp[i-2])
        return dp[n]

# @lc code=end

