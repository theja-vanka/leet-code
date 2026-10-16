class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result: int = 0
        prefix_sum: dict = {
            0: 1
        }
        current_sum: int = 0

        for n in nums:
            current_sum += n
            difference = current_sum - k

            result += prefix_sum.get(difference, 0)
            prefix_sum[current_sum] = prefix_sum.get(current_sum, 0) + 1
        
        return result
        