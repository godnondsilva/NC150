class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        for i in range(len(nums)-k+1):
            cur_max = nums[i]
            for j in range(i+1, i+k):
                cur_max = max(cur_max, nums[j])
            result.append(cur_max)
        return result