class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        res = [0]

        for _ in range(n):
            flipped_res = [1] + (list(map(lambda x: x ^ 1, reversed(res))))
            res = res + flipped_res

        return str(res[k - 1])
