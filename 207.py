from typing import List
from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pm, visited = defaultdict(list), set()
        for c, p in prerequisites: pm[c].append(p)

        def dfs(c):
            if c in visited: return False
            if not pm[c]: return True
            visited.add(c)
            if not all(dfs(p) for p in pm[c]): return False
            pm[c] = []  
            visited.remove(c)
            return True

        return all(dfs(c) for c in range(numCourses))
