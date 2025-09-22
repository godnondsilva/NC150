class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = []
        for x in range(n):
            total = 1
            for y in range(n):
                if x == y: continue
                total *= nums[y]
            result.append(total)
        return result