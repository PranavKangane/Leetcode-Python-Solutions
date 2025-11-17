class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0
        allow = set(allowed)
        for word in words:
            for char in word:
                if char not in allow:
                    count += 1
                    break

        return len(words) - count