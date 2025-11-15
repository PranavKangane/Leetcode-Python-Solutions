class Solution:
    def getLucky(self, s: str, k: int) -> int:
        num = ""
        for ch in s:
            num += str(ord(ch) - ord('a') + 1)

        
        for i in range(k):
            num = str(sum(int(x) for x in num))


        
        return int(num)
            

