class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # keep track of the smallest seen elemetn so far
        # only care about a new day if it:
        # - leads to a bigger profit
        # - is a new canidate for the cheapest day
        minbuy = None
        maxProfit = 0
        for price in prices:
            if minbuy is None:
                minbuy = price
                profit = 0 - minbuy
                continue
            profit = price - minbuy
            minbuy = min(price, minbuy)
            maxProfit = max(profit, maxProfit)
        return maxProfit
            

        