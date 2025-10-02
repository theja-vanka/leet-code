class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:

        drunk_bottles = numBottles
        empty_bottles = numBottles

        while empty_bottles >= numExchange:
            drunk_bottles += 1
            empty_bottles -= numExchange - 1
            numExchange += 1
        
        return drunk_bottles



        

        



            

        