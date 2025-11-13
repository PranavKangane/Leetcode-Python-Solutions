class Solution:
    def largestAltitude(self, gain: List[int]) -> int:

        alt = 0
        maxalt = 0

        for n in gain:
            alt += n
            maxalt = max(alt,maxalt)
        
        return maxalt
