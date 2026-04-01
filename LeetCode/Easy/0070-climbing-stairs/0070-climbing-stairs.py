class Solution:
    def climbStairs(self, n: int) -> int:

        memo: dict = {}
        memo[0] = 1
        memo[1] = 1
        memo[2] = 2


        def dynamic(n):
            if n not in memo:
                memo[n] = dynamic(n-1) + dynamic(n-2)
            return memo[n]

        return dynamic(n) 
        