class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for _ in s:
            if _ == "(" or _ == "[" or _ == "{":
                stack.append(_)
            elif _ == ")" and stack:
                if stack[-1] == "(":
                    stack.pop()
                else:
                    return False
            elif _ == "}" and stack:
                if stack[-1] == "{":
                    stack.pop()
                else:
                    return False
            elif _ == "]" and stack:
                if stack[-1] == "[":
                    stack.pop()
                else:
                    return False
            else:
                return False
        
        return True if len(stack) == 0 else False