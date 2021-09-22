#
# @lc app=leetcode id=127 lang=python3
#
# [127] Word Ladder
#
import collections
from typing import List
# @lc code=start
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)

        if endWord not in word_set:
            return 0

        q1, q2 = collections.deque([beginWord]), collections.deque([endWord])
        visited1, visited2 = set([beginWord]), set([endWord])
        w_len = len(beginWord)
        res = 1
        
        while q1:
            if len(q1) > len(q2):
                q1, q2 = q2, q1
                visited1, visited2 = visited2, visited1
            size = len(q1)
            for i in range(size):
                w = list(q1.pop())
                for j in range(w_len):
                    c = w[j]
                    for k in range(26):
                        w[j] = chr(ord("a") + k)
                        nw = "".join(w)
                        if nw in word_set:
                            if nw in visited2:
                                return res + 1
                            if nw not in visited1:
                                q1.appendleft(nw)
                                visited1.add(nw)
                    w[j] = c
            res += 1
        
        return 0
# @lc code=end

