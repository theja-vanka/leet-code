class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:

        total: int = 0

        for c in set(s):
            first = s.find(c)
            last = s.rfind(c)
            if first < last:
                middle_chars = set(s[first+1:last])
                total += len(middle_chars)
        
        return total

        