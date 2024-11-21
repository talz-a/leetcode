from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1] * n

        def helper(idx):
            if idx >= n:
                return 0
            if dp[idx] != -1:
                return dp[idx]
            dp[idx] = max(nums[idx] + helper(idx + 2), helper(idx + 1))
            return dp[idx]

        return helper(0)
