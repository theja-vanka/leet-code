class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set: set = set()
        left: int = 0
        max_len: int = 0

        for right, character in enumerate(s):
            while character in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(character)
            max_len = max(max_len, right - left + 1)
        return max_len
        