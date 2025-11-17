class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        hashmap = {}
        count = 0
        for n in nums:
            hashmap[n] = hashmap.get(n,0) + 1

        for i, value in hashmap.items():
            pairs = (value * (value - 1)) // 2
            count += pairs


        return count 
        