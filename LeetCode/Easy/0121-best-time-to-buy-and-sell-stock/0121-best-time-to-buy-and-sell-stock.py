class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_profit: int = 0
        min_value:int = float('inf')

        for price in prices:
            if price < min_value:
                min_value = price
            max_profit = max(max_profit, price - min_value)
        
        return max_profit

        

        