from collections import deque
from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        p_set, a_set = set(), set()
        d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        n, m = len(heights), len(heights[0])
        q = deque()

        def inBounds(x, y):
            return 0 <= x < n and 0 <= y < m

        def canFlow(old_x, old_y, new_x, new_y):
            return heights[new_x][new_y] >= heights[old_x][old_y]

        def bfs(queue, visited_set):
            while queue:
                r, c = queue.popleft()
                visited_set.add((r, c))
                for dx, dy in d:
                    new_r, new_c = r + dx, c + dy
                    if (
                        inBounds(new_r, new_c)
                        and canFlow(r, c, new_r, new_c)
                        and (new_r, new_c) not in visited_set
                    ):
                        queue.append((new_r, new_c))

        for c in range(m):
            q.append((0, c))
        for r in range(n):
            q.append((r, 0))
        bfs(q, p_set)

        for c in range(m):
            q.append((n - 1, c))
        for r in range(n):
            q.append((r, m - 1))
        bfs(q, a_set)

        return list(map(list, p_set & a_set))
