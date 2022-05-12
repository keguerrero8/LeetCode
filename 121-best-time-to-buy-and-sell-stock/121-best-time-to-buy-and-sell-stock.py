class Solution(object):
    def maxProfit(self, prices):
        minBuy = float("inf")
        profit = 0
        
        for price in prices:
            if price < minBuy:
                minBuy = price
            currentProfit = price - minBuy
            if currentProfit > profit:
                profit = currentProfit
        
        return profit
        