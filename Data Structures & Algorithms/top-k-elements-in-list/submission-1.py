class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 0:
            return []

        count = {}
        
        for n in nums:
            if n not in count:
                count[n] = 1
            else:
                count[n] += 1
        
        count = list(dict(sorted(count.items(), key = lambda item: item[1], reverse=True)).keys())
        print(count)
        ans = []
        for i in range(k):
            ans.append(count[i])
        return ans