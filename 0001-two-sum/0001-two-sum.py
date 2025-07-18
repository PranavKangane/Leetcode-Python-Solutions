class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        empty = {}
        for index, value in enumerate(nums):
            diff = target - value
            if diff in empty:
                return [empty[diff], index]
            empty[value] = index
