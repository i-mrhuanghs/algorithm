#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
from typing import List
# 暴力解法
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def _generate_prenthesis(left, right, n, s):
            # terminator
            if left == right == n:
                res.append(s)
                return
            # process current logic; left right
            s1 = s + "("
            s2 = s + ")"
            # drill down
            if left < n: # 如果左括号小于n，才能添加左括号
                _generate_prenthesis(left+1, right, n, s1)
            if left >right: # 如果左括号大于右括号，才能添加右括号
                _generate_prenthesis(left, right+1, n, s2)
            # reverse states
        # 第一个是由左括号开始的
        res = []
        _generate_prenthesis(1, 0, n, "(")
        return res
# @lc code=end

"""
from typing import List 
# 暴力解法
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def valid(A):
            bal = 0
            for c in A:
                if c == '(': bal += 1
                else: bal -= 1
                if bal < 0: return False
            return bal == 0
        def _generate_prenthesis(level, m, s):
            # terminator
            if level >= m:
                if valid(s):
                    res.append(s)
                return
            # process current logic; left right
            s1 = s + "("
            s2 = s + ")"
            # drill down
            _generate_prenthesis(level+1, m, s1)
            _generate_prenthesis(level+1, m, s2)
            # reverse states
        res = []
        _generate_prenthesis(0, 2*n, "")
        return res

# 暴力解法改进 减去无用的递归分支
from typing import List
# 暴力解法
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def _generate_prenthesis(left, right, n, s):
            # terminator
            if left == right == n:
                res.append(s)
                return
            # process current logic; left right
            s1 = s + "("
            s2 = s + ")"
            # drill down
            if left < n: # 如果左括号小于n，才能添加左括号
                _generate_prenthesis(left+1, right, n, s1)
            if left >right: # 如果左括号大于右括号，才能添加右括号
                _generate_prenthesis(left, right+1, n, s2)
            # reverse states
        # 第一个是由左括号开始的
        res = []
        _generate_prenthesis(1, 0, n, "(")
        return res
"""