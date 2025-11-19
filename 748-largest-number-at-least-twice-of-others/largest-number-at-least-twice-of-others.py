class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        a = max(nums)
        idx = nums.index(a)

        # we only compare with the second-largest number
        for i, val in enumerate(nums):
            if i != idx and a < 2 * val:
                return -1
        
        return idx

        