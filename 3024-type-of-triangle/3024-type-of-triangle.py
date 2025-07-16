class Solution:
    def triangleType(self, nums: List[int]) -> str:
        myset = set(nums)
        newnums = list(myset)

        a,b,c = sorted(nums)
        if a + b <= c:
            return 'none'
        elif len(newnums) == 1:
            return 'equilateral'
        elif len(newnums) == 2:
            return 'isosceles'
        else:
            return 'scalene'
