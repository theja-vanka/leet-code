class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0
        
        n = len(s)
        dp = [0] * n
        max_length = 0
        
        for i in range(1, n):
            if s[i] == ')':
                # Case 1: The previous character is '(' -> e.g., "..." + "()"
                if s[i-1] == '(':
                    dp[i] = (dp[i-2] if i >= 2 else 0) + 2
                
                # Case 2: The previous character is ')' -> e.g., "..." + "))"
                # We look for a matching '(' before the valid substring ending at i-1
                elif i - dp[i-1] - 1 >= 0 and s[i - dp[i-1] - 1] == '(':
                    # Add the inner valid length, the 2 new matching characters,
                    # and any valid length that came before the matching '('
                    prev_valid = dp[i - dp[i-1] - 2] if (i - dp[i-1] - 2) >= 0 else 0
                    dp[i] = dp[i-1] + 2 + prev_valid
                
                # Keep track of the longest one we've seen so far
                max_length = max(max_length, dp[i])
                
        return max_length