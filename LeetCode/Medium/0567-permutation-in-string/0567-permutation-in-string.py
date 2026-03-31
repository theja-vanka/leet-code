class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        counter_s1 = Counter(s1)
        window = len(s1)

        for i in range(0, len(s2) - window + 1, 1):
            _ = Counter(s2[i:i+window])
            if _ == counter_s1:
                return True
        
        return False
        
        
        