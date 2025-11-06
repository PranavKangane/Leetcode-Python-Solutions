class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        smap = {}
        tmap = {}

        for x in range(len(s)):
            smap[s[x]] = smap.get(s[x],0)+1
        
        for x in range(len(t)):
            tmap[t[x]] = tmap.get(t[x],0)+1
        

        for index, values in tmap.items():
            if index not in smap:
                return index
            elif index in smap:
                if values != smap[index]:
                    return index
