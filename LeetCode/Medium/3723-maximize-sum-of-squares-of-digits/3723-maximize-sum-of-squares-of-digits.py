class Solution:
    def maxSumOfSquares(self, num: int, s: int) -> str:
        
        if s > 9 * num or s < 0:
            return ""
        
        result = []
        for _ in range(num):

            digit = min(9, s)
            result.append(str(digit))
            s -= digit
        
        return "".join(result)