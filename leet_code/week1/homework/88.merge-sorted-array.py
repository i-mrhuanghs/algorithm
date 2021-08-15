#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#

# @lc code=start
from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # 创建三个指针
        i = m-1
        j = n-1
        k = m+n-1
        while i >= 0 or j >= 0:
        # j < 0, i&k向左移
            if j < 0:
                nums1[k] = nums1[i]
                i -= 1
        # j < 0, j&k向左移
            elif i < 0:
                nums1[k] = nums2[j]
                j -= 1
        # i > j, i&k向左移
            elif nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
        # i < j, j&k向左移
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1


# @lc code=end

