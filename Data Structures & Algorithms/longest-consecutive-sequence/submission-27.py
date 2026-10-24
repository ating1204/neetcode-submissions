class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        sort = sorted(nums)
        print(sort)
        m = 1
        k = 1
        for i in range(1, len(nums)):
            if sort[i-1] + 1 == sort[i]:
                k += 1
            elif sort[i-1] == sort[i]:
                continue
            else:
                if m < k:
                    m = k
                k = 1
        if m < k:
            m = k
        return m