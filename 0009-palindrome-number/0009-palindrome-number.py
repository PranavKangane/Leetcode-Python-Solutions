class Solution:
    def isPalindrome(self, x: int) -> bool:
        original = str(x)
        flipped = str(x)
        flipped = flipped[::-1]

        if original == flipped:
            return True
        else:
            return False

        