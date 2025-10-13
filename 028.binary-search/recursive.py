class Solution:
    def search_section(self, l: int, r: int, nums: List[int], target: int) -> int:
        if l>r:
            return -1
        
        m = l+(r-l)//2
        if nums[m] == target:
            return m
        elif nums[m] < target:
            return self.search_section(m+1, r, nums, target)
        else:
            return self.search_section(l, m-1, nums, target)

    def search(self, nums: List[int], target: int) -> int:
        return self.search_section(0, len(nums)-1, nums, target)