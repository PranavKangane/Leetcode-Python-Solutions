class Solution:
    def firstUniqChar(self, s: str) -> int:
        smap = {}

        for x in range(len(s)):
            smap[s[x]] = smap.get(s[x],0)+1

        print(smap)

        for index, value in smap.items():
            if value == 1:
                return s.find(index)
        
        return -1