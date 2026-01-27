class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        left: int = 0
        right: int = 0
        max_len: int = 0
        current_len: int = 0

        save_set: set = set()

        while(right < len(s)):
            if s[right] not in save_set:
                save_set.add(s[right])
                current_len += 1
                right += 1
            else:
                save_set.remove(s[left])
                left += 1
                max_len = max(max_len, current_len)
                current_len -= 1
        
        max_len = max(max_len, current_len)
        
        return max_len


        

        