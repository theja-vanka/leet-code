class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        array_s = [0] * 26
        array_t = [0] * 26

        for _ in s:
            _ = ord(_.lower()) - ord('a')
            array_s[_] += 1
        
        for _ in t:
            _ = ord(_.lower()) - ord('a')
            array_t[_] += 1
        
        return array_s == array_t
        