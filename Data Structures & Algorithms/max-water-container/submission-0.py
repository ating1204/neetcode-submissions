class Solution:
    def maxArea(self, heights: List[int]) -> int:
        a = 0
        b = len(heights) - 1
        area = min(heights[a],heights[b])*(b-a)
        while a < b:
            if heights[a] < heights[b]:
                a += 1
            else:
                b -= 1
            if min(heights[a],heights[b])*(b-a) > area:
                area = min(heights[a],heights[b])*(b-a)
        return area