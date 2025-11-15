class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        cmap = {}
        tmap = {}

        for cs, ct in zip(s,t):
            if cs not in cmap and ct not in tmap:
                cmap[cs] = ct
                tmap[ct] = cs
            else:
                if cmap.get(cs) != ct or tmap.get(ct) != cs:
                    return False
            
        return True
