class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        zeroCount, total = 0, 1
        for num in nums:
            if num: total *= num
            else: zeroCount+=1

        if zeroCount > 1: return [0]*n
        
        result = []
        for num in nums:
            if zeroCount:
                if num == 0:
                    result.append(total)
                else:
                    result.append(0)
            else:
                result.append(total//num)

        return result