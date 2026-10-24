class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        j = 0
        while j < len(nums):
            prod = 1
            for i in range(len(nums)):
                if i != j:
                    prod *= nums[i]
            res.append(prod)
            j+= 1
        return res