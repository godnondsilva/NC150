class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water = 0
        for l in range(len(heights)):
            for r in range(len(heights)):
                water = abs(l-r) * min(heights[l], heights[r])
                max_water = max(max_water, water)
        return max_water