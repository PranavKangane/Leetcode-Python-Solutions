class Solution:
    def romanToInt(self, s: str) -> int:
        
        valdic = {'I':1, 'V':5, 'X': 10, 'L': 50, 'C':100, 'D':500, 'M':1000,
        'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD':400, 'CM':900}

        total = 0
        for i in range(len(s)-1):
            if valdic[s[i]] < valdic[s[i+1]]:
                total -= valdic[s[i]]
            else:
                total += valdic[s[i]]
            print(total)

        total += valdic[s[-1]]

        return total
     

