class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = None

        for value in nums:
            if count == 0:
                candidate = value
            count = count + (1 if value==candidate else -1)

        return candidate