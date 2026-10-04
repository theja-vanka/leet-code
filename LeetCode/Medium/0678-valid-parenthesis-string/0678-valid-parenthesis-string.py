class Solution:
    def checkValidString(self, s: str) -> bool:
        open_stack = []
        star_stack = []
        
        # Step 1: Loop through the string with indices
        for i, char in enumerate(s):
            # Your code here for handling '(', '*', and ')'
            if char == "(":
                open_stack.append(i)
            elif char == "*":
                star_stack.append(i)
            else:
                if open_stack:
                    open_stack.pop()
                elif star_stack:
                    star_stack.pop()
                else:
                    return False
            
        # Step 2: Match remaining '(' and '*'
        # Your code here
        while open_stack and star_stack:
            open_bracket = open_stack.pop()    
            star_bracket = star_stack.pop()
            if open_bracket > star_bracket:
                return False
        
        # Step 3: Return if it's valid
        return len(open_stack) == 0