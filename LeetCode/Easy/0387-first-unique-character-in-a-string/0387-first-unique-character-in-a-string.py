class Solution:
    def firstUniqChar(self, s: str) -> int:

        hashmap: dict = {}

        for i, c in enumerate(s):
            if c not in hashmap:
                hashmap[c] = [i]
            else:
                hashmap[c].append(i)
        
        for key, value in hashmap.items():
            if len(value) == 1:
                return value[0]
        
        return -1
        