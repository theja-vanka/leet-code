class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        min_cost: int = float('inf')
        max_profit: int = 0

        for price in prices:
            if price < min_cost:
                min_cost = price
            else:
                profit = price - min_cost
                if profit > max_profit:
                    max_profit = profit
        
        return max_profit

        

        