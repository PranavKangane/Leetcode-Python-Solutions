class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        result = []
        for n in nums:
            if n % 2 == 0:
                result.append(0)
            else:
                result.append(1)
        
        newresult = sorted(result)
        return newresult

        