class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hashmap: dict = {}

        for s in strs:
            s_t = tuple(sorted(s))

            if s_t not in hashmap:
                hashmap[s_t] = [s]
            else:
                hashmap[s_t].append(s)

        return list(hashmap.values())