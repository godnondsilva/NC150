class Solution:
    def isPalindrome(self, s: str) -> bool:
        lst = [c for c in s.lower() if c.isalnum()]
        return lst == lst[::-1]