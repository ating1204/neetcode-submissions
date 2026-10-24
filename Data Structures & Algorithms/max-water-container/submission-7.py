class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        res = 0
        while l < r:
            h = min(heights[r], heights[l])
            area = (r - l) * h
            res = max(area, res)
            if h == heights[r]:
                while l < r and heights[r] <= h:
                    r -= 1
            else: #either min is l or both eq
                while l < r and heights[l] <=h:
                    l += 1

        return res