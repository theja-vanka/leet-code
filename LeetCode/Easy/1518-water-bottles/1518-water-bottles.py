class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        
        total_bottles = numBottles
        remainder = 0
        while numBottles:
            quotient, remainder = divmod(numBottles + remainder, numExchange)
            total_bottles += quotient
            numBottles = quotient

        return total_bottles            
        