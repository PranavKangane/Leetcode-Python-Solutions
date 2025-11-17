class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        numout = [0 for x in range(len(nums2))]
        stack = []

        for i in range(len(nums2)-1,-1,-1):
            while stack and stack[-1] <= nums2[i]:
                stack.pop()

            if not stack:
                numout[i] = -1
            else:
                numout[i] = stack[-1]
            stack.append(nums2[i])

        dic1 = dict(zip(nums2,numout))
        res = [dic1[x] for x in nums1]

        return res



