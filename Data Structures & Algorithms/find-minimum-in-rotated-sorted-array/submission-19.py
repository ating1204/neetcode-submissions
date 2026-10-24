class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] < nums[-1]:
            return nums[0]
        
        a = 0
        b = len(nums) - 1
        m = 0
        
        #search left
        while a < b:
            m = (a + b) // 2
            if a == m:
                return nums[m+1]
            elif m == b:
                return nums[m]

            if nums[m] > nums[0]: #m on left side of sorted array
                a = m #search right
            else: #m on right side
                b = m
        return nums[0]

