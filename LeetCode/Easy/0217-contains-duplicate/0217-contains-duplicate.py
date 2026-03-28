class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        hashmap: dict = {}

        for index, num in enumerate(nums):
            if num not in hashmap:
                hashmap[num] = [index]
            else:
                return True

        return False
        
        