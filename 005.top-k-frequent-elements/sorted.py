class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for i in range(len(nums)):
            counter[nums[i]] = counter.get(nums[i], 0) + 1

        arr = []
        for num, cnt in counter.items():
            arr.append([cnt, num])
        arr.sort()
        
        result = []
        while len(result) < k:
            result.append(arr.pop()[1])
        return result