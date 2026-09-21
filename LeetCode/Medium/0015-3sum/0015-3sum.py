class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        result = set()

        for index in range(len(nums) - 2):
            if index > 0 and nums[index] == nums[index - 1]:
                continue
            
            seen = set()
            for j in range(index + 1, len(nums)):
                complement = -nums[index]-nums[j]

                if complement in seen:
                    result.add((nums[index], complement, nums[j]))

                seen.add(nums[j])
        
        return [list(r) for r in result]