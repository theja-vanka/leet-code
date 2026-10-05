class Solution:
    def myAtoi(self, s: str) -> int:
        # 1. Remove leading whitespaces
        s = s.lstrip()
        if not s:
            return 0
        
        # 2. Check the sign
        sign = 1
        i = 0
        if s[0] == '-':
            sign = -1
            i += 1
        elif s[0] == '+':
            i += 1
            
        # 3. Convert digits to integer
        result = 0
        while i < len(s) and s[i].isdigit():
            # ord() gives the ASCII value, so subtracting ord('0') gets the actual number
            digit = ord(s[i]) - ord('0')
            result = result * 10 + digit
            i += 1
            
        # Apply sign
        result *= sign
        
        # 4. Handle 32-bit integer overflow limits
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1
        
        if result < INT_MIN:
            return INT_MIN
        if result > INT_MAX:
            return INT_MAX
            
        return result