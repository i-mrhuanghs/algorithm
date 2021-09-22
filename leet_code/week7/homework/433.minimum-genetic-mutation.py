#
# @lc app=leetcode id=433 lang=python3
#
# [433] Minimum Genetic Mutation
#
from typing import List
from math import inf
# @lc code=start
class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        # end不在bank中，则不合法，返回-1
        if end not in bank: return -1

        res = [inf]

        # 计算两个基因序列的偏差数
        def diff(start,end):   
            count = 0
            for i in range(8):
                if start[i] != end[i]:
                    count += 1
            return count
        
        # 深度优先
        def helper(start,count,bank):
            temp = diff(start,end)

            # 找到目标基因序列，返回变化次数
            if temp == 0:
                res.append(count)
                return

            # bank为空，即没有更多的变化可能，返回inf占位
            if not bank:
                count.append(inf)

            for b in range(len(bank)):
                # 发现bank中有刚好偏差1的基因序列，删去对应序列，继续寻找
                if diff(start,bank[b]) ==1:
                    helper(bank[b],count+1,bank[:b]+bank[b+1:])
        
        helper(start,0,bank)

        # 如果只有inf存在，则没有找到变化的路线
        if min(res) == inf: return -1

        return min(res)
# @lc code=end

