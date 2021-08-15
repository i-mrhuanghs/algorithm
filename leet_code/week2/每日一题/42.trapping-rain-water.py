#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#

# @lc code=start
from os import stat
from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        stack = []
        for i,h in enumerate(height):
            while stack and h > height[stack[-1]]:
                top = stack.pop()
                if not stack:
                    break
                left = stack[-1]
                width = i - left - 1
                heig = min(height[left], h) - height[top]
                ans += width * heig
            stack.append(i)
        return ans
        
# @lc code=end

