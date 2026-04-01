class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if t == "": return ""

        hashmap_t: dict = Counter(t)
        hashmap_s: dict = {}

        have, need = 0, len(hashmap_t)

        res, res_len = [-1, -1], float('inf')
        l = 0
        for r in range(len(s)):
            c = s[r]
            hashmap_s[c] = hashmap_s.get(c, 0) + 1

            if c in hashmap_t and hashmap_t[c] == hashmap_s[c]:
                have += 1

                while have == need:
                    if (r - l + 1) < res_len:
                        res = [l , r]
                        res_len = (r - l + 1)
                    hashmap_s[s[l]] -= 1
                    if s[l] in hashmap_t and hashmap_s[s[l]] < hashmap_t[s[l]]:
                        have -= 1  
                    l += 1

        l, r = res 

        return s[l:r+1] if res_len != float('inf') else ""

        

        

        



        