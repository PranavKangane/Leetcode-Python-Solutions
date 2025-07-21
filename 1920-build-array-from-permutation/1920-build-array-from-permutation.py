class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        newnums = []
        newnums += [nums[nums[i]] for i in range(len(nums))]

        return newnums
