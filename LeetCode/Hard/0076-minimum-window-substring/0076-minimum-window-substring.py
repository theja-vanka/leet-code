class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if len(s) < len(t): return ""
        map_t: dict = {}

        for char in t:
            map_t[char] = map_t.get(char, 0) + 1
        
        map_s: dict = {}
        l = 0
        need, have = len(map_t), 0
        min_window = [-1, -1]
        min_length = float('inf')

        for r in range(len(s)):
            char = s[r]
            map_s[char] = map_s.get(char, 0) + 1

            if char in map_t and map_t[char] == map_s[char]:
                have += 1
            
            while have == need:
                if (r - l + 1) < min_length:
                    min_length = (r - l + 1)
                    min_window = [l, r]
                
                map_s[s[l]] -= 1
                if s[l] in map_t and map_t[s[l]] > map_s[s[l]]:
                    have -= 1
                l += 1
            
        l, r = min_window
        return s[l:r + 1] if min_length != float('inf') else ""
