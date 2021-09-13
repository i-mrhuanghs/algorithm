#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1: return 1
        if n == 2: return 2
        res = [0, 1, 2] + [-1]* (n-2)
        for i in range(3,n+1):
            res[i] = res[i-2] + res[i-1]
        return res[n]

        
# @lc code=end

