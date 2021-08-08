#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#

# @lc code=start
from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        left, right =[0], [0]
        for h in height:left.append(max(left[-1], h))
        for h in height[::-1]:right.append(max(right[-1], h))
        right.reverse()
        return sum(max(min(left[i],right[i+1])-height[i],0) for i in range(len(height)))

# @lc code=end

