class Solution:
    def addDigits(self, num: int) -> int:
        while len(str(num)) > 1:
            digits = [int(x) for x in str(num)]
            newnum = sum(digits)
            num = newnum

        if num == 0:
            return 0
        else:
            return num


