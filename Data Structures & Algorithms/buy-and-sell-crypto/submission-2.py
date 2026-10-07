class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # integer array prices where prices[i] is the price of a stock
        # on ith day

        # we need to choose a day when to buy a neetcoin
        # and day in future to sell it

        # return max profit we can achieve
        # we want to aim for the lowest amount possible

        max_profit = 0

        lowest_price = prices[0]
        max_price = prices[0]
        max_profit = 0

        for price in prices:
            lowest_price = min(price, lowest_price)
            max_price = max(price, max_price)

            curr_profit = price - lowest_price
            max_profit = max(curr_profit, max_profit)
        
        return max_profit


    
        