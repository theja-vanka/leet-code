class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:

        empty_bottles = numBottles
        total_drunk = numBottles
        while empty_bottles >= numExchange:
            empty_bottles = empty_bottles - numExchange
            total_drunk += 1
            numExchange += 1
            empty_bottles += 1
        
        return total_drunk



        

        



            

        