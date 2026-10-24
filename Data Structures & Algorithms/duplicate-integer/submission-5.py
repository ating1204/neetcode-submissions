class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        distinctNums = set(nums)
        if len(distinctNums) < len(nums):
            return True
        return False