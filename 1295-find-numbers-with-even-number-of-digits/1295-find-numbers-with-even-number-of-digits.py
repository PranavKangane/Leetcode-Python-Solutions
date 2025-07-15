class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        evens = [x for x in nums if len(str(x)) % 2 == 0]
        counter = 0

        for x in evens:
            counter += 1

    
        return counter

    

        