class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        counter: int = [0] * 26

        if len(s) != len(t):
            return False
        

        for _s in s:
            counter[ord(_s) - ord('a')] += 1
        
        for _t in t:
            counter[ord(_t) - ord('a')] -= 1
        
        return counter == [0] * 26