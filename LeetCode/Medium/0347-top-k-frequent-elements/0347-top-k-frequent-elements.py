class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        hashmap: dict = {}
        freq : List[list] = [[] for i in range(len(nums) + 1)]

        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1

        for key, value in hashmap.items():
            freq[value].append(key)
        
        result: list = []

        for i in range(len(freq) - 1, 0, -1):
            for v in freq[i]:
                result.append(v)

                if len(result) == k:
                    return result
                    



        