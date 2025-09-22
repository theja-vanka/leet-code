class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_map<char, int> hashmap;
        int left = 0, maxLen = 0;
        for (int right = 0; right < s.size(); ++right) {
            if (hashmap.count(s[right]) && hashmap[s[right]] >= left) {
                left = hashmap[s[right]] + 1;
            }
            hashmap[s[right]] = right;
            maxLen = max(maxLen, right - left + 1);
        }
        return maxLen;
    }
};