class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        set<char> result;
        int left = 0;
        int right = 0;
        int maxLen = 0;
        
        while(right < s.size()){
            if(result.find(s[right]) != result.end()){
                result.erase(s[left]);
                left += 1;
            }
            else{
                result.insert(s[right]);
                maxLen = max(right - left + 1, maxLen);
                right += 1;
            }
        }
        return maxLen;
        
    }
};