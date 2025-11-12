class Solution:
    def frequencySort(self, s: str) -> str:
        res = [[] for i in range(len(s)+1)]

        hashmap = {}
        for i in range(len(s)):
            hashmap[s[i]] = hashmap.get(s[i],0) + 1

        for i, v in hashmap.items():
            res[v].append(i)

        final = ""
        for i in range(len(res)-1,-1,-1):
            for values in res[i]:
                final += i*values
        
        return final
