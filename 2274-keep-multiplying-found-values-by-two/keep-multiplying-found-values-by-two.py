class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:

        newnum = original
        while newnum in nums:
            newnum = 2 * newnum


        return newnum

        