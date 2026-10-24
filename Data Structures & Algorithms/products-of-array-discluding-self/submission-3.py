class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        prod = 1
        
        def prod(nums: List[int], a, b):
            if a == b:
                return 1
            prod = 1
            for i in range(a, b):
                prod *= nums[i]
            return prod
        
        end = len(nums)

        for i in range(len(nums)):
            res.append(prod(nums, 0, i) * prod(nums, i+1, end))
        return res
            
