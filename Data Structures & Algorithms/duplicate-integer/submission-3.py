class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hs = set({})
        for x in nums:
            n = len(hs)
            hs.add(x)
            if len(hs) == n:
                return True
        return False