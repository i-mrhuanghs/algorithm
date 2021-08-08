#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#

# @lc code=start
from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(1,len(digits)+1):
            if (digits[-i]+1)%10 != 0:
                digits[-i] += 1
                return digits
            digits[-i]=0
        return [1]+digits
        

# @lc code=end

# @before-stub-for-debug-end