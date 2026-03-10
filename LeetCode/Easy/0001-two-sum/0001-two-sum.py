class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hashmap: dict = {}

        for index, value in enumerate(nums):
            if value in hashmap:
                return [hashmap[value], index]
            hashmap[target - value] = index
        
        return [-1, -1]
        