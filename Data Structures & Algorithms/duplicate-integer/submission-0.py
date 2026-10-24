class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dups = []
        for i in range(len(nums)):
            if nums[i] in dups:
                return True
            else:
                dups.append(nums[i])
        return False