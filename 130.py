from typing import List
from collections import deque

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        n, m = len(board), len(board[0])
        q = deque()

        for i in range(n):
            if board[i][0] == "O":
                q.append((i, 0))
            if board[i][m - 1] == "O":
                q.append((i, m - 1))
        for i in range(m):
            if board[0][i] == "O":
                q.append((0, i))
            if board[n - 1][i] == "O":
                q.append((n - 1, i))

        while q:
            r, c = q.popleft()
            if board[r][c] != "O":
                continue
            board[r][c] = "T"
            for dy, dx in d:
                new_r, new_c = r + dy, c + dx
                if 0 <= new_r < n and 0 <= new_c < m and board[new_r][new_c] == "O":
                    q.append((new_r, new_c))

        for i in range(n):
            for j in range(m):
                if board[i][j] == "O":
                    board[i][j] = "X"  
                elif board[i][j] == "T":
                    board[i][j] = "O" 
