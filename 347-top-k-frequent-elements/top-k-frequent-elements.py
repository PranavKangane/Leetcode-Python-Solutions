class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for i in nums:
            hashmap[i] = hashmap.get(i, 0) + 1   # this loop ends here

        freq = [[] for i in range(len(nums) + 1)] 
        

        for index, values in hashmap.items():
            freq[values].append(index)

        res = []
        for i in range(len(freq) - 1, 0, -1):  # iterate from 6 to 1
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
       
         
        

    

      