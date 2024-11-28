from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {i: [] for i in range(numCourses)}
        for c, p in prerequisites: adj[c].append(p)
        visit, cycle = set(), set()
        res = []  

        def dfs(c):
            if c in cycle: return False
            if c in visit: return True

            visit.add(c)
            for p in adj[c]:
                if not dfs(p): return False

            cycle.remove(c)
            visit.add(c)
            res.append(c)
            return True

        for i in range(numCourses):
            if not dfs(i): return []  

        return res  
