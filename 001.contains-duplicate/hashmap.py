class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = {}
        for i in range(len(nums)):
            if (seen.get(nums[i])):
                return True
            seen[nums[i]] = 1
        return False