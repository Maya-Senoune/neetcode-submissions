class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
                
        left = 1
        right = max(piles)
        
        while left < right: 
            k = (left+right)//2

            totalHours = 0
            for x in piles:
                totalHours += math.ceil(x/k)
            
            if totalHours > h:
                left = k + 1
            else:
                right = k

        return left




            

            
            

