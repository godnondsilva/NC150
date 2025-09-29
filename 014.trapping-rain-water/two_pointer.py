class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        l_max, r_max = height[l], height[r]
        total = 0
        while l<r:
            if l_max < r_max:
                l+=1
                l_max = max(l_max, height[l])
                total += l_max - height[l]
            else:
                r-=1
                r_max = max(r_max, height[r])
                total += r_max - height[r]
        return total