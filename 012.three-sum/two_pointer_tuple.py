class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        nums.sort()
        for x in range(len(nums)):
            i,j=x+1, len(nums)-1
            while i<j:
                total = nums[x] + nums[i] + nums[j]
                if total == 0:
                    result.add((nums[x], nums[i], nums[j]))
                    i+=1
                    j-=1
                elif total > 0:
                    j-=1
                else:
                    i+=1
        return list(result)