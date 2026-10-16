class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        
        t_map: dict = {}
        for char in t:
            t_map[char] = t_map.get(char, 0) + 1
        
        have, need = 0, len(t_map)
        result_indexes, result = [-1, -1], float('inf')

        s_map: dict = {}
        l = 0
        for r in range(len(s)):
            char = s[r]
            s_map[char] = s_map.get(char, 0) + 1

            if char in t_map and s_map[char] == t_map[char]:
                have += 1
            
            while have == need:
                if (r - l + 1) < result:
                    result_indexes = [l, r]
                    result = min(result, r - l + 1)

                s_map[s[l]] -= 1
                if s[l] in t_map and s_map[s[l]] < t_map[s[l]]:
                    have -= 1
                l += 1
            
        l, r = result_indexes
        return s[l:r+1] if result != float("inf") else ""