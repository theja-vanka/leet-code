class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hashmap: dict = {}

        for string in strs:
            ss = tuple(sorted(string))
            if ss not in hashmap:
                hashmap[ss] = []
            hashmap[ss].append(string)
        
        return [value for _, value in hashmap.items()]


        