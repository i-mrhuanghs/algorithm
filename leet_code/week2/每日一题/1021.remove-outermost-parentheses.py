#
# @lc app=leetcode id=1021 lang=python3
#
# [1021] Remove Outermost Parentheses
#

# @lc code=start
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        count = 0
        ans = ''
        for i in range(len(s)):
            if s[i] == '(':
                ans += '(' if count > 0 else ''
                count += 1
            if s[i] == ')':
                ans += ')' if count > 1 else ''
                count -= 1
        return ans
# @lc code=end

