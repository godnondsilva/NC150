class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        for speed in range(1, max(piles)+1):
            total = 0
            for pile in piles:
                total += math.ceil(pile/speed)
            if total <= h:
                return speed
        return -1