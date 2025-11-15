class Solution:
    def countDigits(self, num: int) -> int:

        digits = [int(x) for x in str(num)]

        count = 0

        for x in digits:
            if num % x == 0:
                count += 1

        return count
        

