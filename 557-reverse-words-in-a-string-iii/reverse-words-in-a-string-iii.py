class Solution:
    def reverseWords(self, s: str) -> str:
        l1 = s.split()
        for x in range(len(l1)):
            a = list(l1[x])
            left = 0
            right = len(a) -1
            while left < right:
                a[left],a[right] = a[right],a[left]
                left += 1
                right -= 1
            
            reverse = "".join(a)
            l1[x] = reverse
        
        return " ".join(l1)
            
        

            