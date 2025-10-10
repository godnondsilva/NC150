class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = []
        for i in range(len(temperatures)):
            to_check = temperatures[i]
            first_warmer_dist = 0
            for j in range(i, len(temperatures)):
                if temperatures[j] > to_check:
                    first_warmer_dist = j-i
                    break
            result.append(first_warmer_dist)
        return result