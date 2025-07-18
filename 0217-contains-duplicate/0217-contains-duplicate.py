class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        original = len(nums)
        newnums = set(nums)
        print(original)
        print(len(list(newnums)))
        if original > len(list(newnums)):
            return True
        else:
            return False