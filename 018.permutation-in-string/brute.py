class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_sorted = sorted(s1)
        for i in range(len(s2)-len(s1)+1):
            s2_sub_sorted = sorted(s2[i:i+len(s1)])
            print(s1_sorted, s2_sub_sorted)
            if s1_sorted == s2_sub_sorted:
                return True
        return False