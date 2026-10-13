class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        right = max(piles)
        left = 1

        while left < right:
            k = (right + left) // 2
            total = 0
            for pile in piles:
                total += pile//k
                if pile % k != 0:
                    total += 1

            if total <= h:
                right = k
            else:
                left = k+1
        
        return right