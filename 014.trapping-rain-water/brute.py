class Solution:
    def trap(self, height: List[int]) -> int:
        n, total = len(height), 0
        for i in range(n):
            l_max = r_max = height[i]
            for j in range(i):
                l_max = max(l_max, height[j])
            for j in range(i+1, n):
                r_max = max(r_max, height[j])
            total += min(l_max, r_max) - height[i]
        return total