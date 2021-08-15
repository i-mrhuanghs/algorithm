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
        # 定义两个指针 fast,slow
        # 遍历一次
        # fast和slow一开始指向同一个位置，如果fast为真不为0，和slow交换位置，其实是原地不动的，然后两个指针同时往前走
        # 如果这次是0 fast往前走就会留下slow，slow指向0
        j = 0
        for i in range(len(nums)):
            if nums[i]:
                nums[j], nums[i] = nums[i], nums[j]
                j += 1


# @lc code=end

