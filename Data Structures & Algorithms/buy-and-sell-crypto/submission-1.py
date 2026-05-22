class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prof = 0
        ln = 0
        rn = 1
        while rn < len(prices):
            if prices[rn] <= prices[ln]: 
                ln = rn
                rn +=1
            else: 
                if prices[rn] - prices[ln] > prof: prof = prices[rn] - prices[ln]
                rn += 1
        return prof
            
            
