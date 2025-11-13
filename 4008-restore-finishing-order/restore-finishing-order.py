class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:

        hashmap = {person: i for i, person in enumerate(order)}
        

        freq = []
        for f in friends:
            freq.append((hashmap[f], f))

        freq.sort()
        result = []
        for rank,pair in freq:
            result.append(pair)
        
        return result

      
       
            