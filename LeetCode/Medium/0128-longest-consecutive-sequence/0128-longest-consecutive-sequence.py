class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        num_set = set(nums)   
        result:int = 0
        for n in num_set:
            if n-1 not in num_set:
                consecutive = 0
                while n + consecutive in num_set:
                    consecutive += 1
                result = max(result, consecutive)
        return result

        