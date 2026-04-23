class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        frequency_list = [[] for i in range(len(nums) + 1)]
        hashmap: dict = {}

        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1
        
        for key, value in hashmap.items():
            frequency_list[value].append(key)
        
        result = []
        for index in range(len(frequency_list) - 1, -1, -1):
            for n in frequency_list[index]:
                result.append(n)
                if len(result) == k:
                    return result
            

        
                    



        