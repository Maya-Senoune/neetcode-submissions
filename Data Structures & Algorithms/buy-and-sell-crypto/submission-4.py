class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        left = 0
        right = left + 1
        maxprofit = 0

        while right < len(prices):
            
            if prices[left] > prices[right]:
                left = right
                right = right + 1
            
            else:
                currMax = prices[right] - prices[left]
                maxprofit = max(currMax,maxprofit)
                right = right + 1  

        return maxprofit             

