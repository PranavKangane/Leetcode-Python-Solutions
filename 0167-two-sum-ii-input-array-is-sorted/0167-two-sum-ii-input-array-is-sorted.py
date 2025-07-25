class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers)-1
        while left < right:
            total = int(numbers[left]) + int(numbers[right])
            if total == target:
                return [left+1, right+1]
            elif total < right:
                left += 1
            else:
                right -= 1
        