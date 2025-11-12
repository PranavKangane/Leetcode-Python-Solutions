class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        s = min(nums)
        m = max(nums)
        a = [i for i in range(s,m+1)]
        c = set(a) - set(nums)
        newlist = sorted(list(c))
        return newlist