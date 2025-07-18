class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        maxlength = 0
        left, right = 0,0
        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            
            seen.add(s[right])
            maxlength = max(maxlength, right - left + 1)

        return maxlength


        