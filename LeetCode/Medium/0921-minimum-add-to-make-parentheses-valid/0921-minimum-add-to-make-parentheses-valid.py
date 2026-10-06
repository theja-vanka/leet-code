class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        for b in s:
            if b == "(":
                stack.append(b)
            else:
                if stack and stack[-1] == "(":
                    stack.pop()
                else:
                    stack.append(")")
        
        return len(stack)