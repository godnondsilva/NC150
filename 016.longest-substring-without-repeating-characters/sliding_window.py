class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_substr = 0
        uniques = set()
        l=0
        for r in range(len(s)):
            while s[r] in uniques:
                uniques.remove(s[l])
                l+=1
            uniques.add(s[r])
            longest_substr = max(longest_substr, r-l+1)
        return longest_substr