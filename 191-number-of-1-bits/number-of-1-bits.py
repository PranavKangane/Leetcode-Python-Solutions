class Solution:
    def hammingWeight(self, n: int) -> int:
        num = str(bin(n))
        return num.count('1')