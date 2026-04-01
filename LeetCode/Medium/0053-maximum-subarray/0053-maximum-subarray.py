class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        max_sum: int = nums[0]
        current_sum: int = 0

        for num in nums:
            if current_sum < 0:
                current_sum = 0
            current_sum += num
            max_sum = max(max_sum, current_sum)
    
        return max_sum
