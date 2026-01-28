class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        nums: set = set(nums)
        max_streak: int = 0
        current_streak: int = 0
        current_number: int = 0

        for num in nums:
            if num - 1 not in nums:
                current_streak = 1
                current_number = num

                while current_number + 1 in nums:
                    current_number += 1
                    current_streak += 1
            
            max_streak = max(current_streak, max_streak)
        
        return max_streak


        
        