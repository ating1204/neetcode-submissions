class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ht = {}
        for i, x in enumerate(nums):
            y = target - x
            if y in ht:
                return [ht.get(y), i]
            ht[x] = i
        return [-1, -1]
                