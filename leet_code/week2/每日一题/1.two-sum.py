#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable = {}
        for i, num in enumerate(nums):
            if target-num in hashtable:
                return i,hashtable[target-num]
            hashtable[num]=i # 先判断，后赋值，避免重复
# @lc code=end

