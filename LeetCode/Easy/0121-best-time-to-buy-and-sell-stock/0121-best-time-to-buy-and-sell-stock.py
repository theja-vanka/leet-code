class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_profit: int = 0 
        min_value:int = float('inf')
        for index, value in enumerate(prices):
            if value < min_value:
                min_value = value
            max_profit = max(max_profit, value - min_value)
        
        return max_profit

        

        