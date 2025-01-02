class Solution:
    def confusingNumber(self, n: int) -> bool:
        invalid_nums = {"2", "3", "4", "5", "7"}
        valid_map = {"0": "0", "1": "1", "6": "9", "8": "8", "9": "6"}
        
        n_str = str(n)
        
        if any(ch in invalid_nums for ch in n_str):
            return False
        
        transformed = "".join(valid_map[ch] for ch in reversed(n_str))
        
        return transformed != n_str
