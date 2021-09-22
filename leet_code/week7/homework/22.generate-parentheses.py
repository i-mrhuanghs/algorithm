#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#
from typing import List
# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        cur_str = ''

        def dfs(cur_str, left, right, n):
            if left == n and right == n:
                res.append(cur_str)
                return
            if left < right:
                return

            if left < n:
                dfs(cur_str + '(', left + 1, right, n)

            if right < n:
                dfs(cur_str + ')', left, right + 1, n)

        dfs(cur_str, 0, 0, n)
        return res
# @lc code=end

