class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
      
        stack = []
        n = len(nums)
        numout = [-1] * n

        for i in range(2*len(nums)-1,-1,-1):
            cur = nums[i % n]
            while stack and stack[-1] <= cur:
                stack.pop()
            
            if i < len(nums):
                if not stack:
                    numout[i] = -1
                else:
                    numout[i] = stack[-1]
            
            stack.append(cur)

        return numout
            
                

        