class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        left, right = 0, len(nums)
        sortednum = sorted(nums)
        print(sortednum)
        for i in range(len(sortednum)):
            if i != sortednum[i]:
                return i
            else:
                continue

        return len(nums)
                

     