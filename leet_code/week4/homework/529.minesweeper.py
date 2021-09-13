#
# @lc app=leetcode id=529 lang=python3
#
# [529] Minesweeper
#
from typing import List
# @lc code=start
class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        m, n = len(board), len(board[0])
        dx = [0, 1, 0, -1, 1, 1, -1, -1]
        dy = [1, 0, -1, 0, -1, 1, 1, -1]

        def digit(row, col):
            cnt = 0
            for i in range(8):
                nrow, ncol = row + dx[i], col + dy[i]
                if m > nrow >= 0 and n > ncol >= 0 and board[nrow][ncol] == 'M':
                    cnt += 1
            return cnt
        
        # DFS
        def reveal(row, col):
            cnt = digit(row, col)
            if cnt == 0:
                board[row][col] = 'B'
                for i in range(8):
                    nrow, ncol = row + dx[i], col + dy[i]
                    if m > nrow >= 0 and n > ncol >= 0 and board[nrow][ncol] == 'E':
                        reveal(nrow, ncol)
            
            else:
                board[row][col] = str(cnt)

        row, col = click
        if board[row][col] == 'M':
            board[row][col] = 'X'
        else:
            reveal(row, col)
        return board
# @lc code=end

