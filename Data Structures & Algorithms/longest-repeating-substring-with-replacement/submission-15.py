class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        letters = set()
        for ch in s:
            letters.add(ch)
        res = 0
        n = len(s)
        for ch in letters:
            l = 0
            valid = 0
            for r in range(n):
                if s[r] == ch:
                    valid += 1
                while (r - l + 1) - valid > k:
                    if s[l] == ch:
                        valid -= 1
                    l += 1
                res = max(res, (r - l + 1))
        return res


          