class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        x = 0
        y = 1
        while x < len(nums) - 2:
            while y < len(nums) - 1:
                diff = 0 - nums[x] - nums[y]
                if diff in nums[y+1:]:
                    sol = sorted([nums[x], nums[y], diff])
                    if sol not in res:
                        res.append(sol)
                y += 1
            x += 1
            y = x + 1
        return res
                
