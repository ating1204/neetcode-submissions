class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = res = maxF = 0
        count = {}
        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            maxF = max(count[s[r]], maxF) #you only care abt curr elem bc thats the only one that could possible change max rn
            while (r - l + 1) - maxF > k:
                count[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)
        
        return res