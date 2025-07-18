class Solution:
    def isPalindrome(self, s: str) -> bool:
        news = ""
        news += "".join([ a.lower() for a in s if a.isalnum()])
        print(news)
        left, right = 0, len(news) - 1
        while left < right:
            if news[left] != news[right]:
                return False
            else:
                left += 1
                right -= 1
        
        return True

        if left == right:
            left += 1
            return True
          

      
