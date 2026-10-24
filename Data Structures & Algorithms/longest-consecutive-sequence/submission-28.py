class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = sorted(nums)
        m = 0
        for x in s:
            if (x-1) not in s: #start of seq
                k = 1
                while (x+1) in s:
                    k += 1
                    x += 1
                if k > m:
                    m = k
        return m
