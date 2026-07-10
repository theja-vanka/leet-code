class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hashmap: dict = {}

        for index, num in enumerate(nums):
            if num not in hashmap:
                hashmap[target-num] = index
            else:
                return [hashmap[num], index]
        