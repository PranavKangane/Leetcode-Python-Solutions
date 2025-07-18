class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        unique = set(nums)
        n = len(nums)
        original = set(range(1,n+1))
        return list(original.difference(unique))
        

            
