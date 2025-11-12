class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashmap = defaultdict(list)

        for ind,val in enumerate(nums):
                hashmap[val].append(ind)

        for ind, val in hashmap.items():
            if len(val) >= 2:
                for x in range(len(val)-1):
                    diff = abs(val[x] - val[x+1])
                    if k >= diff:
                        return True
        return False

        
            
