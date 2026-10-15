class Solution:
    def compress(self, chars: list[str]) -> int:
        
        count = 0
        pointer = 0
        i = 0
        current_char = chars[0]

        while i < len(chars):
            if current_char == chars[i]:
                count += 1
            else:
                chars[pointer] = current_char
                pointer += 1
                if count > 1:
                    count = str(count)
                    for c in count:
                        chars[pointer] = c
                        pointer += 1
                current_char = chars[i]
                count = 1
            i += 1
        
        chars[pointer] = current_char
        pointer += 1
        if count > 1:
            count = str(count)
            for c in count:
                chars[pointer] = c
                pointer += 1

        return pointer
        