class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        hashmap = defaultdict(list)

        for index, v in enumerate(nums):
            if v == val:
                hashmap[v].append(index)

        for index in reversed(hashmap[val]):
            nums.pop(index)

        return len(nums)
 


    
        

