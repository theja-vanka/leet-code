class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:

        nums.sort()
        length: int = len(nums)

        result: list = []
        
        for index, value in enumerate(nums):
            if index > 0 and nums[index - 1] == value:
                continue
            
            left = index + 1
            right = length - 1
            while left < right:
                three_sum =  value + nums[left] + nums[right]
                if three_sum == 0:
                    result.append([value, nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
                elif three_sum < 0:
                    left += 1
                else:
                    right -= 1
            
        return result
                