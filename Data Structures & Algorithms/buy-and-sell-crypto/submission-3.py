class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        lowest_price = prices[0]
        max_profit = 0

        for price in prices:
            lowest_price = min(price, lowest_price)

            curr_profit = price - lowest_price
            max_profit = max(curr_profit, max_profit)
        
        return max_profit


    
        