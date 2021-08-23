#
# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#

# @lc code=start
from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        left = right = 0
        while right < n:
            # left 指针停留在0值
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            # right 指针一直走，和left零值指针换位做准备
            right += 1

# @lc code=end
"""
[1, 2, 0, 3, 12] 1 1

[1, 2, 0, 3, 12] 2 2

[1, 2, 0, 3, 12] 2 3

[1, 2, 3, 0, 12] 3 4

[1, 2, 3, 12, 0] 4 5
"""

"""
[0, 1, 0, 3, 12] 0 1

[1, 0, 0, 3, 12] 1 2

[1, 0, 0, 3, 12] 1 3

[1, 3, 0, 0, 12] 2 4

[1, 3, 12, 0, 0] 3 5

"""