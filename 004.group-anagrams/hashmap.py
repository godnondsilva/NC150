class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for cur in strs:
            counter = [0]*26
            for ch in cur:
                counter[ord(ch)-ord('a')] += 1
            result[tuple(counter)].append(cur)
        return list(result.values())