#
# @lc app=leetcode id=122 lang=python3
#
# [122] Best Time to Buy and Sell Stock II
#

# @lc code=start
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        n = len(prices)
        for i in range(1,n):
            ans += max(0, prices[i] - prices[i - 1])
        return ans

# @lc code=end
"""
# 贪心算法只能用于计算最大利润，计算的过程并不是实际的交易过程
# 把每个大于0的区间加到一起就等于 总利润
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        n = len(prices)
        for i in range(1,n):
            ans += max(0, prices[i] - prices[i - 1])
        return ans
"""
