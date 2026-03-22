class Solution:
    def compress(self, chars: List[str]) -> int:

        length: int = len(chars)
        if length == 1:
            return 1
        

        current_char = chars[0]
        write = 1
        count = 1

        for index in range(1, length, 1):
            if current_char == chars[index]:
                count += 1
            else:
                current_char = chars[index]
                if count > 1:
                    for cs in str(count):
                        chars[write] = cs
                        write += 1
                chars[write] = current_char 
                write += 1
                count = 1
        
        if count > 1:
            for cs in str(count):
                chars[write] = cs
                write += 1

        return write
        

        
        