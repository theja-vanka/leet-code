class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        hashmap: dict = {}

        if len(s) != len(t):
            return False

        for _s in s:
            hashmap[_s] = hashmap.get(_s, 0) + 1
        
        for _t in t:
            if _t not in hashmap:
                return False
            else:
                hashmap[_t] -= 1
                if hashmap[_t] == 0:
                    del hashmap[_t]
        
        return True
        