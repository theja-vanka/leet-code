class Solution {
public:
    int maxBottlesDrunk(int numBottles, int numExchange) {

        int emptyBottles = numBottles;
        int drunkBottles = numBottles;

        while(emptyBottles >= numExchange){
            drunkBottles += 1;
            emptyBottles -= numExchange - 1;
            numExchange += 1;
        }

        return drunkBottles;
        
    }
};