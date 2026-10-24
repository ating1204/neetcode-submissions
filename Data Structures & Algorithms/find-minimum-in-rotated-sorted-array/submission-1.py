class Solution:
    def findMin(self, nums: List[int]) -> int:
        min = 0
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                min = i
        return nums[min]