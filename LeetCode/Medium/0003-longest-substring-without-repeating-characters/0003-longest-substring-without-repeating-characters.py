class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        left: int = 0
        right: int = 0
        max_len: int = 0
        char_map: dict = {}

        while right < len(s):
            if s[right] not in char_map:
                char_map[s[right]] = right
            else:
                left = max(left, char_map[s[right]] + 1)
                char_map[s[right]] = right
            max_len = max(max_len, right - left + 1)
            right += 1
        
        return max_len


        

        