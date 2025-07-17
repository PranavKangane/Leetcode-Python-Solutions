class Solution:
    def reverseVowels(self, s: str) -> str:
        front = ''
        back = ''
        vowels = set('aeiouAEIOU')
        left, right = 0, len(s)- 1
        while left < right:
            if s[left] not in vowels:
                front += s[left]
                left += 1
            else:
                if s[right] not in vowels:
                    back += s[right]
                    right -= 1
                else:
                    front += s[right]
                    back += s[left]
                    left += 1
                    right -= 1
        
        if left == right:
            front += s[left]
            left += 1

        newstring = front + back[::-1]
        return newstring
