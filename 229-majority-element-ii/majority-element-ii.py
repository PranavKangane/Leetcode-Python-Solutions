class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = {}
        n = len(nums)

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        res = []
        for key, value in freq.items():
            if value > n // 3:
                res.append(key)

        return res





        