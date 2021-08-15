#
# @lc app=leetcode id=258 lang=python3
#
# [258] Add Digits
#

# @lc code=start
class Solution:
    def addDigits(self, num: int) -> int:
        sum = 0
        while num >= 10:
            dight = num % 10
            num = num // 10
            sum += dight
            if num < 10:
                num += sum
                sum = 0
        return num
# @lc code=end

