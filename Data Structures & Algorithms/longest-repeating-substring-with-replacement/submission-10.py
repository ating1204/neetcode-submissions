class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        chars = set(s)
        res = 0

        for ch in chars:
            r = l = valid = 0

            while r < len(s):
                if s[r] == ch:
                    valid += 1

                while (r - l + 1) - valid > k:
                    if s[l] == ch:
                        valid -= 1
                    l += 1
                res = max(res, r - l + 1)
                r += 1
        return res