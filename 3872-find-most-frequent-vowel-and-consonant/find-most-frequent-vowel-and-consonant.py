class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowel = {'a':0, "e":0, "i":0, "o":0, "u":0}
        con = {}

        for char in range(len(s)):
            if s[char] in vowel:
                vowel[s[char]] = vowel.get(s[char],0) + 1
            else:
                con[s[char]] = con.get(s[char],0)+ 1

        vfreq = [[] for x in range(len(s)+1)]
        vcon = [[] for x in range(len(s)+1)]

        for i, v in vowel.items():
            vfreq[v].append(i)
        
        for i, v in con.items():
            vcon[v].append(i)

        vmax = 0
        cmax = 0

        for i in range(len(vfreq) - 1, -1, -1):
            if vfreq[i]:
                vmax = i
                break

        for i in range(len(vcon) - 1, -1, -1):
            if vcon[i]:
                cmax = i
                break

        return vmax + cmax
        

    