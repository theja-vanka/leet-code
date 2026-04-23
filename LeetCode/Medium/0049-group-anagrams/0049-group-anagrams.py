class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hashmap: dict = {}
        result = []
        for s in strs:
            s_t = tuple(sorted(s))

            if s_t not in hashmap:
                hashmap[s_t] = [s]
            else:
                hashmap[s_t].append(s)
        
        for value in hashmap.values():
            result.append(value)

        return result