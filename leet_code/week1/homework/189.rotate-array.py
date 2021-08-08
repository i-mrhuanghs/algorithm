#
# @lc app=leetcode id=189 lang=python3
#
# [189] Rotate Array
#

# @lc code=start
from typing import List
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums[: ] = (nums[i] for i in range(-(k % len(nums)), len(nums) - k % len(nums)))
# @lc code=end

