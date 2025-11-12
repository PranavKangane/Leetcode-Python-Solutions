class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = list("aeiouAEIOU")
        news = list(s)
        left = 0
        right = len(s) - 1
        while left < right:
            if news[left] in vowels and news[right] in vowels:
                news[left],news[right] = news[right],news[left]
                left += 1
                right -= 1
            elif news[left] in vowels and news[right] not in vowels:
                right -= 1
            elif news[right] in vowels and news[left] not in vowels:
                left += 1
            else:
                left += 1
                right -= 1
        return "".join(news)