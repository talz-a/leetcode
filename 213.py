from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(a):
            rob1, rob2 = 0, 0
            for x in a:
                temp = max(rob1 + x, rob2)
                rob1 = rob2
                rob2 = temp
            return rob2

        return max(nums[0], helper(nums[1:]), helper(nums[:-1]))
