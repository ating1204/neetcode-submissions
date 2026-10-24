class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        #run two sum for each num in list --> n* O(n) --> O(n^2)
        res = []
        uniqSols = set()
        for i in range(len(nums) - 2):
            target = -nums[i]
            l, r = i + 1, len(nums) - 1
            while l < r:
                if nums[l] + nums[r] == target and (nums[i], nums[l], nums[r]) not in uniqSols:
                    res.append([nums[i], nums[l], nums[r]])
                    uniqSols.add((nums[i], nums[l], nums[r]))
                    l += 1
                else:
                    if nums[l] + nums[r] > target:
                        r -= 1
                    else:
                        l += 1

        return res
