class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        snums = sorted(nums)
        res = []

        for i in range(len(snums)-2):
            if i > 0 and snums[i] == snums[i-1]:
                continue
            
            target = snums[i]
            left = i + 1
            right = len(snums) -1 
            while left < right:
                total = snums[left] + snums[right]
                if total + target == 0:
                    res.append([target,snums[left],snums[right]])
                    left += 1
                    right -= 1
                    while left < right and snums[left] == snums[left - 1]:
                        left += 1
                    while left < right and snums[right] == snums[right + 1]:
                        right -= 1
                elif total + target > 0:
                    right -= 1
                elif total + target < 0:
                    left += 1
        return res


        
            