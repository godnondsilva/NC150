class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        longest, streak = 0, 0
        nums.sort()
        curr, i = nums[0], 0
        while i < len(nums):
            if curr != nums[i]:
                curr = nums[i]
                streak = 0
            while i < len(nums) and nums[i] == curr:
                i += 1
            streak +=1
            curr += 1
            longest = max(longest, streak)
        return longest