class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        nums = [num**2 for num in nums]
        nums = sorted(nums)
        return nums
        