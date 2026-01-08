class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        smap, tmap = {}, {}

        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            smap[s[i]] = smap.get(s[i],0) + 1
            tmap[t[i]] = tmap.get(t[i],0) + 1

        for count in smap:
            if smap[count] != tmap.get(count,0):
                return False

        return True
