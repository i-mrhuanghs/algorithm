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
"""
# python 双指针
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        #首先要对g 和 s排序：题中没有说明输入是有序序列
        g.sort()
        s.sort()
        #两个指针分别指向两个列表的末尾
        r_g = len(g) - 1
        r_s = len(s) - 1
        count = 0
        #循环条件
        while r_g >= 0 and r_s >= 0:
            #两个指针分别指向两个列表的末尾如果满足`s[r_s] >= g[r_g]`，则都向前移动
            if s[r_s] >= g[r_g]:
                count += 1
                r_g -= 1
                r_s -= 1
            #否则只需要移动g的指针
            else:
                r_g -= 1
        return count
"""
