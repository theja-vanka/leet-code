class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        
        hashmap: dict = {}

        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1
        
        heap = [(v, k) for k,v in hashmap.items()]

        heapq.heapify(heap)

        while len(heap) > k:
            heapq.heappop(heap)
        
        return [h[1] for h in heap]
