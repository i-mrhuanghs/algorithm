#
# @lc app=leetcode id=412 lang=python3
#
# [412] Fizz Buzz
#

# @lc code=start
from typing import List
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        output = []
        for i in range(1,n+1):
            if i%15 == 0:
                output.append('FizzBuzz')
            elif i%3 == 0:
                output.append('Fizz')
            elif i%5 == 0:
                output.append('Buzz')
            else:
                output.append(str(i))
        return output
# @lc code=end

