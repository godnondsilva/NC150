class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        buckets = [[] for i in range(len(nums)+1)]

        for num in nums:
            counter[num] = counter.get(num, 0) + 1

        for num, cnt in counter.items():
            buckets[cnt].append(num)
        
        result = []
        for i in range(len(buckets)-1, 0, -1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result