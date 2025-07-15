class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = {}
        for char in nums:
            if char in count:
                count[char] += 1
            else:   
                count[char] = 1
        
        for key,value in count.items():
            if value == 1:
                return key
            else:
                continue
        
