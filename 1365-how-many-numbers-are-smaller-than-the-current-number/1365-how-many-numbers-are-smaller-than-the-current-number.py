class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sort = {}
        for i, value in enumerate(sorted(nums)):
            if value not in sort:
                sort[value] = i
        return [sort[num] for num in nums]
