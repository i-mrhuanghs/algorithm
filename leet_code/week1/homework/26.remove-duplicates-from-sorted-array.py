#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # 处理空值的情况：
        # 为空 则返回数组列表为0
        # 处理非空的情况：
        # 两个非空指针 数组长度
        # 慢指针位置改变：
        # 当发现快指针遍历数组的不同值时，把值赋给慢指针指向的地方，慢指针的位置改变
        # 快指针位置改变：每次循环都改变
        if not nums:
            return 0
        n = len(nums)
        fast = slow = 1
        while fast < n:
            if nums[fast] != nums[fast-1]:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow
# @lc code=end
