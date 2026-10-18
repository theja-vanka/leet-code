class Solution:
    def maximumCandies(self, candies: list[int], k: int) -> int:

        left, right = 1, max(candies)
        result = 0

        while left <= right:
            mid = (left + right) // 2
            children_fed = sum(c // mid for c in candies)
            
            if children_fed >= k:
                result = mid   
                left = mid + 1
            else:
                right = mid - 1
            
        return result