class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = res = 0
        valid = 0
        for r in range(len(nums)):
            if nums[r]:
                valid += 1
            while (r - l + 1) - valid > k:
                if nums[l]:
                    valid -= 1
                l += 1
            res = max(res, (r - l + 1))
        
        return res