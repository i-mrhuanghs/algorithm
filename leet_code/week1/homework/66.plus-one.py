#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#

# @lc code=start
from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digitStr = "".join(map(str,digits))
        return map(int,str(int(digitStr)+1))
# @lc code=end

