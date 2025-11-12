class Solution:
    def compress(self, chars: List[str]) -> int:
        read = 0
        strs = []
        while read < len(chars):
            current = chars[read]
            count = 0

            while read < len(chars) and chars[read] == current:
                count += 1
                read += 1

            if count == 1:
                strs.append(current)
            else:
                strs.append(current)
                for digit in str(count):
                    strs.append(digit)
        
        chars[:] = strs
        return len(strs)