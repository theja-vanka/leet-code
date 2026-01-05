class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        i = len(num) - 1
        carry = 0
        res = []

        while i >= 0 or k > 0 or carry > 0:
            if i >= 0:
                carry += num[i]
                i -= 1
            carry += k % 10
            k //= 10
            res.insert(0, carry % 10)
            carry //= 10

        return res