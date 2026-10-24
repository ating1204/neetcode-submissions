class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dups = {}
        dist = {}
        i = 0
        for x in nums:
            if x not in dist:
                dist[x] = i
            else:
                dups[x] = i
            i += 1
        for x in dist:
            y = target - x
            if x == y and y in dups:
                return [dist[x], dups[y]]
            elif x != y and y in dist:
                return [dist[x], dist[y]] if dist[x] < dist[y] else [dist[y], dist[x]]
        return []

                