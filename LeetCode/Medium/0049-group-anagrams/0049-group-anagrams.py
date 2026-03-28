class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hashmap: dict = {}

        for s in strs:
            _ = tuple(sorted(s))

            if _ not in hashmap:
                hashmap[_] = [s]
            else:
                hashmap[_].append(s)
        
        result = []

        for value in hashmap.values():
            result.append(value)

        return result
        