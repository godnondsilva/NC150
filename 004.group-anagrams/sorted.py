class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for cur in strs:
            sorted_s = "".join(sorted(cur))
            result[sorted_s].append(cur)
        return list(result.values())