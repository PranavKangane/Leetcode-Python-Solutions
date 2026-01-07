class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashmap = defaultdict(list)

        for index, value in enumerate(nums):
            hashmap[value].append(index)
        
        for index, values in hashmap.items():
            if len(values) >= 2:
                for x in range(len(values)-1):
                    diff = abs(values[x] - values[x+1])
                    if k >= diff:
                        return True
        
        return False



        
            
