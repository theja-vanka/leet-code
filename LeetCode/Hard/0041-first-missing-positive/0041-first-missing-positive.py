class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        length: int = len(nums)
        for i in range(length):
            if nums[i] <= 0 or nums[i] > length:
                nums[i] = length + 1
        
        for i in range(length):
            while 1 <= nums[i] <= length and nums[i] != nums[nums[i] - 1]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1] 
            
        for i in range(length):
            if nums[i] != i + 1:
                return i + 1
        
        return length + 1

        
