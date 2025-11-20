from math import gcd
class Solution:
    def findGCD(self, nums: List[int]) -> int:
        small = min(nums)
        large = max(nums)
        return math.gcd(small,large)
        