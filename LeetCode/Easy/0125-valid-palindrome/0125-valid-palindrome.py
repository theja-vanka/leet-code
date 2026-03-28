class Solution:
    def isPalindrome(self, s: str) -> bool:

        cleaned_string: str = ""

        for c in s:
            if c.isalnum():
                cleaned_string += c.lower()


        left: int = 0
        right: int = len(cleaned_string) - 1

        while left < right:
            if cleaned_string[left] != cleaned_string[right]:
                return False
            left += 1
            right -= 1
        
        return True
    
