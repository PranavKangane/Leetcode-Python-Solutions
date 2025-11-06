class Solution:
    def isPalindrome(self, s: str) -> bool:
     news = list(s)
     newl = [x.lower() for x in news if x.isalnum()]
     list2 = newl.copy()
     left = 0
     right = len(list2)-1
     while left < right:
        list2[left],list2[right] = list2[right],list2[left]
        left += 1
        right -= 1

     if newl == list2:
        return True
     else:
        return False


     
    

