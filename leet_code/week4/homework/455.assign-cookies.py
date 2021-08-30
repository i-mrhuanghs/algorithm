#
# @lc app=leetcode id=455 lang=python3
#
# [455] Assign Cookies
#

# @lc code=start
from typing import List
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        sn = len(s)
        gn = len(g)
        if sn == 0:
            return 0
        s.sort(reverse=True)
        g.sort(reverse=True)
        res = 0
        gi = 0
        si = 0
        while True:
            if gi>=gn or si>=sn:
                break
            if s[si] >= g[gi]:
                res += 1
                si += 1
            gi += 1
        return res
# @lc code=end

