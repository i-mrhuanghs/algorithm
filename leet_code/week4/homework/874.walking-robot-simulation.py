#
# @lc app=leetcode id=874 lang=python3
#
# [874] Walking Robot Simulation
#

# @lc code=start
from typing import List
class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        x = y = di = 0
        obstacles_set = set(map(tuple, obstacles))
        ans = 0
        for cmd in commands:
            if cmd == -2:
                di = (di + 3) % 4
            elif cmd == -1:
                di = (di + 1) % 4
            else:
                for _ in range(cmd):
                    if (x+dx[di], y+dy[di]) not in obstacles_set:
                        x += dx[di]
                        y += dy[di]
                        ans = max(ans, x*x+y*y)
        return ans
    
# @lc code=end
"""
class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        dx, dy, x, y = 0, 1, 0, 0
        distance = 0
        obs_dict = {}
        for obs in obstacles:
            obs_dict[tuple(obs)] = 0
        for com in commands:
            if com == -2:
                dx, dy = -dy, dx
            elif com == -1:
                dx, dy = dy, -dx
            else:
                for j in range(com):
                    next_x = x + dx
                    next_y = y + dy
                    if (next_x, next_y) in obs_dict:
                        break
                    x, y = next_x, next_y
                    distance = max(distance, x*x + y*y)
        return distance
"""
