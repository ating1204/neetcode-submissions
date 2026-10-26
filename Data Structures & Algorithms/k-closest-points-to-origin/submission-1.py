import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = []
        res = []
        for x,y in points:
            d = x**2 + y**2
            dist.append([d, [x,y]])
        for _ in range(k):
            heapq.heapify(dist)
            x = heapq.heappop(dist)
            res.append(x[1])
            
        return res