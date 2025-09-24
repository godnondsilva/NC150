class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsMap = defaultdict(int)
        longest = 0
        for num in nums:
            if not numsMap[num]:
                numsMap[num] = numsMap[num - 1] + numsMap[num + 1] + 1
                numsMap[num - numsMap[num - 1]] = numsMap[num]
                numsMap[num + numsMap[num + 1]] = numsMap[num]
                longest = max(longest, numsMap[num])
        return longest