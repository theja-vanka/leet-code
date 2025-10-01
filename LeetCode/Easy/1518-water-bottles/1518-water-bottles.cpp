class Solution {
public:
    int numWaterBottles(int numBottles, int numExchange) {

        int maximumBottles = numBottles;
        int remainder = 0;
        int quotient = 0;
        while(numBottles > 0){
            quotient = (numBottles + remainder) / numExchange;
            remainder = (numBottles + remainder) % numExchange;
            maximumBottles += quotient;
            numBottles = quotient;
        }
        return maximumBottles;
    }
};