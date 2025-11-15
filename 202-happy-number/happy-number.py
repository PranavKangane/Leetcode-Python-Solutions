class Solution:
    def isHappy(self, n: int) -> bool:
        
        passlist = []
        while n not in passlist:
            passlist.append(n)
            digits = [int(x) for x in str(n)]
            sq = list(map(lambda x: x*x, digits))
            if sum(sq) == 1:
                return True
            else:      
                n = sum(sq)
        return False






        