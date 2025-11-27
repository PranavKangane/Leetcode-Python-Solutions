class Solution:
    def reverseBits(self, n: int) -> int:
        nums = bin(n)[2:].zfill(32)
        return int(nums[::-1],2)
    
