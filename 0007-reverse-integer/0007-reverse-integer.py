class Solution:
    def reverse(self, x: int) -> int:
        if x > 0:
            nums = str(x)
            nums = nums[::-1]
            reversed_num = int(nums)
        elif x < 0:
            nums = str(abs(x))
            nums = nums[::-1]
            newnums = "-" + nums
            reversed_num = int(newnums)
        else:
            return 0

        # ✅ Check for 32-bit signed integer overflow
        if reversed_num < -2**31 or reversed_num > 2**31 - 1:
            return 0
        
        return reversed_num