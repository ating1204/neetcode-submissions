class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        chars = set(s) #{X,Y}
        res = 0

        for ch in chars:
            l = valid = 0

            for r in range(len(s)):
                if s[r] == ch:
                    valid += 1
                
                while (r - l + 1) - valid > k:
                    res = max(res, r - l)
                    if s[l] == ch:
                        valid -= 1
                    l += 1
            res = max(res, r - l + 1) 
        return res
            

