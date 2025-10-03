class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_map = {}
        for c in s1:
            s1_map[c] = s1_map.get(c, 0) + 1
        
        for i in range(len(s2)):
            s2_map, count = {}, 0
            for j in range(i, len(s2)):
                s2_map[s2[j]] = s2_map.get(s2[j], 0) + 1
                count1_value = s1_map.get(s2[j], 0)
                if s2_map[s2[j]] > count1_value:
                    break
                if s2_map[s2[j]] == count1_value:
                    count += 1
                if count == len(s1_map):
                    return True
        return False