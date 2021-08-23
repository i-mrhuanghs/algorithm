#
# @lc app=leetcode id=77 lang=python3
#
# [77] Combinations
#

# @lc code=start
from typing import List
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        comb = []

        def backtrack(index: int):
            for i in range(index, n + 1):
                comb.append(i)
                if len(comb) == k:
                    ans.append(comb.copy())
                else:
                    backtrack(i + 1)
                comb.pop()

        backtrack(1)
        return ans
            
# @lc code=end

"""
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def backtrace(i,tmp):
            if len(tmp) == k:
                res.append(tmp)
                return
            for j in range(i,n+1):
                backtrace(j+1,tmp+[j])
        backtrace(1,[])
        return res

"""