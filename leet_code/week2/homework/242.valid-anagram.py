#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
class Solution: #hash table 实现
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        counts = [0] * 26
        for i in range(len(s)):
            counts[ord(s[i]) - ord("a")] += 1
            counts[ord(t[i]) - ord("a")] -= 1
        for i in counts:
            if i != 0:
                return False
        return True
        
# @lc code=end

