class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        lst_len: int = len(nums)
        set_len: int = len(set(nums))

        if set_len < lst_len:
            return True
        return False