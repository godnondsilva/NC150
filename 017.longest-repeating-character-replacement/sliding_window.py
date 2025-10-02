class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_repl = 0
        chars = set(s)
        for c in chars:
            count = l = 0
            for r in range(len(s)):
                if s[r] == c:
                    count+=1
                while (r-l+1) - count > k:
                    if s[l] == c:
                        count-=1
                    l+=1
                max_repl = max(max_repl, r-l+1)
        return max_repl