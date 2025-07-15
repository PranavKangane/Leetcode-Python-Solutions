class Solution:
    def isValid(self, word: str) -> bool:
        vowels = ('aeiouAEIOU')
        
        if len(word) >= 3 and word.isalnum():
             hasvowel = any(char in vowels for char in word)
             hasconsonant = any(char.isalpha() and char not in vowels for char in word)
             return hasvowel and hasconsonant
        else:
            return False
          


         