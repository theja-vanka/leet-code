class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        hashmap: dict = {}

        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1
        
        heap = []

        for key, value in hashmap.items():
            heapq.heappush(heap, (value, key))
            if len(heap) > k:
                heapq.heappop(heap)
        
        return [value for key, value in heap]

        
                    



        