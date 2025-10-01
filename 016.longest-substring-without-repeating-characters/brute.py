class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_substr = 0
        for i in range(len(s)):
            uniques = set()
            for j in range(i, len(s)):
                if s[j] in uniques:
                    break
                uniques.add(s[j])
            longest_substr = max(longest_substr, len(uniques))
        return longest_substr