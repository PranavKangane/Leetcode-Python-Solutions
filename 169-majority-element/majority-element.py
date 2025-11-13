class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        s = set(nums)
        count = 0
        val = 0

        for i in s:
            c = nums.count(i)
            if c >= count:
                count = c
                val = i
        
        return val 
