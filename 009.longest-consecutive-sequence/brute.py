class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        numsSet = set(nums)
        for num in nums:
            streak = 0
            while (num+streak) in numsSet:
                streak+=1
            longest = max(longest, streak)
        return longest