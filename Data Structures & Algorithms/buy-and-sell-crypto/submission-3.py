class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        ma = 0
        s = 0
        e = 1

        while (e < len(prices)):
            if prices[s] > prices[e]:
                s = e
                e = e + 1
            elif prices[s] < prices[e]:
                if prices[e] - prices[s] > ma:
                    ma = prices[e] - prices[s]
                e = e + 1
            else:
                e = e + 1
        
        return ma




        