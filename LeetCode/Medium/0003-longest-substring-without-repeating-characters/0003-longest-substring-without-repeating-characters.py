class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        hashmap: dict = {}
        left = 0
        right = 0
        max_len = 0

        while right < len(s):
            if s[right] not in hashmap:
                hashmap[s[right]] = right
            else:
                left = max(left, hashmap[s[right]] + 1) 
                hashmap[s[right]] = right
            max_len = max(max_len, right - left + 1)
            right += 1
        return max_len
        