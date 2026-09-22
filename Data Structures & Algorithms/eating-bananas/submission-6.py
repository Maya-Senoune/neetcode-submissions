class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lower = 1
        upper = max(piles)

        while lower < upper:
            k = (lower + upper)//2

            total = sum(math.ceil(pile/k)for pile in piles)


            if total > h:
                lower = k + 1

            elif total <= h:
                upper = k 

            
        return upper
