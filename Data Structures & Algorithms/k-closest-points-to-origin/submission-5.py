class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []
        res = []
        for x,y in points:
            d = -(x**2 + y**2)
            heapq.heappush(maxHeap, [d, x, y])
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)

        while maxHeap:
            d, x, y = heapq.heappop(maxHeap)
            res.append([x,y])
        return res
            
            