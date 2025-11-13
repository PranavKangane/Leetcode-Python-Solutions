class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        new = [0] * n

        for i in range(n):
            new[(i + k) % n] = nums[i]

        nums[:] = new

        