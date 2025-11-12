class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxval = max(candies)
        b = list(map(lambda x: x+extraCandies,candies))
        res = [True if x >= maxval else False for x in b]
        return res
        