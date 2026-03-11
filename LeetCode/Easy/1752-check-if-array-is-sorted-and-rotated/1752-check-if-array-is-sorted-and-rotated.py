class Solution:
    def check(self, nums: List[int]) -> bool:

        breaks: int = 0
        n: int = len(nums)

        for i in range(n):
            if nums[i] > nums[(i+1) % n]:
                breaks += 1
            if breaks > 1:
                return False
        return True



        

        