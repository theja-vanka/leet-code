class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        
        hashmap: dict = {}

        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1
        
        heap = []
        for key, value in hashmap.items():
            heapq.heappush(heap, (value, key))

            if len(heap) > k:
                heapq.heappop(heap)
        
        return [key for _, key in heap]
