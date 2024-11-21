class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        new_k = k
        res = 0
        l, r = 0, 0
        letter_count = {}

        while l <= r:
            if s[l] == s[r]:
                letter_count[s[l]] = letter_count.get(s[l], 0) + 1
                res += 1
            elif s[l] != s[r] and new_k > 0:
                new_k -= 1
                letter_count[s[r]] += 1
            else:
                while letter_count[s[l]] > k and l < len(s):
                    l += 1
                    letter_count[s[l]] -= 1

        return res
