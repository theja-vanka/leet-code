class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        hashmap: dict = {}

        for num in nums:
            if num not in hashmap:
                hashmap[num] = num
            else:
                return True
        return False
        