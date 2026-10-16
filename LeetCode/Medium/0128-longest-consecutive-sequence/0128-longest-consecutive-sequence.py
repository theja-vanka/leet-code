class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        set_nums: set = set(nums)
        longest_consecutive_length: int = 0

        for num in set_nums:
            if num - 1 not in set_nums:
                current_length = 0
                while num + current_length in set_nums:
                    current_length += 1
                longest_consecutive_length = max(longest_consecutive_length, current_length)
        
        return longest_consecutive_length
        

        