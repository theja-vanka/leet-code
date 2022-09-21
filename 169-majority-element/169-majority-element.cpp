class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int count = 0;
        int candidate;
        for(auto num: nums){
            if(count == 0){
                candidate = num; 
            }
            if(candidate == num){
                count += 1;
            }
            else{
                count -= 1;
            }  
        }
        return candidate;     
    }   
};