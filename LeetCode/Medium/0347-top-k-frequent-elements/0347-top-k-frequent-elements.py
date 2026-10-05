class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        
        heap = []
        freq = {}

        for num in nums:
            freq[num] = freq.get(num,0)+1
        
        for num, count in freq.items():
            heapq.heappush(heap,(count, num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        return [x for i, x in heap]
