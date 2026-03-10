class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:

        carry: int = k
        for index in range(len(num)-1, -1, -1):
            carry, num[index] = divmod(num[index] + carry, 10)
        

        while carry:
            carry, base = divmod(carry, 10)
            num.insert(0, base)
        
        return num

        
        