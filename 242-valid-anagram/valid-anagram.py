class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        smap = {}
        tmap = {}

        for x in range(len(s)):
            smap[s[x]] = smap.get(s[x],0)+1

        for x in range(len(t)):
            tmap[t[x]] = tmap.get(t[x],0)+1

        if smap == tmap:
            return True
        else:
            return False