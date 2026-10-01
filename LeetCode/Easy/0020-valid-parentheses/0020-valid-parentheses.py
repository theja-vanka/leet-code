class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for _ in s:
            if _ == "(" or _ == "[" or _ == "{":
                stack.append(_)
            else:
                if not stack:
                    return False
                pop = stack.pop()
                if _ == ")" and pop != "(":
                    return False
                elif _ == "}" and pop != "{":
                    return False
                elif _ == "]" and pop != "[":
                    return False
                
        return True if len(stack) == 0 else False