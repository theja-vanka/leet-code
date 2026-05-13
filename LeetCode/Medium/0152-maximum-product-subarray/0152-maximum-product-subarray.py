class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = max(nums)

        current_max = 1
        current_min = 1

        for n in nums:
            temp = n*current_max
            current_max = max(n*current_max, n*current_min, n)
            current_min = min(temp, n*current_min, n)
            result = max(current_max, result)
        return result