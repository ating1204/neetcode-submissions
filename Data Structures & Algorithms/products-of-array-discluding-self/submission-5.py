class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        count = 0
        for x in nums:
            if x == 0:
                count += 1
            else:
                prod *= x
        
        res = []

        if count > 1: return [0] * len(nums)

        for i in range(len(nums)):
            if count == 1:
                if nums[i] != 0:
                    res.append(0)
                else:
                    res.append(prod)
            else:
                res.append(int(prod / nums[i]))
        return res

            
