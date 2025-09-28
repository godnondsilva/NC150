class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i,j = 0,len(heights)-1
        max_water = 0
        while i<j:
            curr_water = min(heights[i], heights[j]) * abs(i-j)
            max_water = max(curr_water, max_water)
            if heights[i] > heights[j]:
                j-=1
            else:
                i+=1
        return max_water