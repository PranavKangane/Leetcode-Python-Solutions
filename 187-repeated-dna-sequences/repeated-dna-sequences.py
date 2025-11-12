class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        hashmap = {}
        for i in range(len(s)-9):
            a = s[i:i+10]
            hashmap[a] = hashmap.get(a,0) + 1
        res = []        
        for i,v in hashmap.items():
            if v >= 2:
                res.append(i)

        return res
