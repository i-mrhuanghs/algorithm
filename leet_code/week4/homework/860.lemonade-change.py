#
# @lc app=leetcode id=860 lang=python3
#
# [860] Lemonade Change
#

# @lc code=start
from collections import defaultdict
from typing import List
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change_dill = defaultdict(int)
        for i in bills:
            change_dill[i] += 1
            diff = i - 5
            while diff:
                if diff >= 10 and change_dill[10]:
                    change_dill[10] -= 1
                    diff -= 10
                elif diff >=5 and change_dill[5]:
                    change_dill[5] -= 1
                    diff -= 5
                else:
                    return False
        return True
# @lc code=end

