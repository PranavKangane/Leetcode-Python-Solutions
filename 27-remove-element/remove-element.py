class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        hashmap = defaultdict(list)

        for i, v in enumerate(nums):
            if v == val:
                hashmap[v].append(i)  # This line needs to be indented
                
        for idx in reversed(hashmap[val]):
                del nums[idx]

        return len(nums)


    
        

