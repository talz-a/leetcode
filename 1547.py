class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        dp = {}
        
        def dfs(i, j):
            if j - i <= 1: return 0
            if (i , j) in dp: return dp[(i, j)]
            res = float("inf")
            for c in cuts:
                if i < c < j:
                    cost = (j - i) + dfs(i, c) + dfs(c, j)
                    res = min(res, cost)
            res = res if res != float("inf") else 0
            dp[(i, j)] = res
            return res

        return dfs(0, n)
