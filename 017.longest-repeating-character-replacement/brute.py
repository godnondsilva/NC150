class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_repl = 0
        for i in range(len(s)):
            counter, max_count = {}, 0
            for j in range(i, len(s)):
                counter[s[j]] = counter.get(s[j], 0) + 1
                max_count = max(max_count, counter[s[j]])
                if j-i+1 - max_count <= k:
                    max_repl = max(max_repl, j-i+1)
        return max_repl