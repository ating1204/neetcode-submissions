class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ind = {}
        for i, n in enumerate(nums):
            ind[n] = i
        for i in range(len(nums)):
            x = nums[i]
            y = target - x
            if y in ind and ind[y] != i:
                return [i, ind[y]]
            
 
                