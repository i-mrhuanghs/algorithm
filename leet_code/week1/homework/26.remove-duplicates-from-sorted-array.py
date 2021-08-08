#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        tem = list(set(nums))
        tem.sort()
        nums[:len(tem)] = tem
        return len(tem)
# @lc code=end

