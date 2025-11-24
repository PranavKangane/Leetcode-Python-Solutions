class Solution:
    def repeatedCharacter(self, s: str) -> str:
        hashmap = {}
        for char in s:
            hashmap[char] = hashmap.get(char,0) + 1
            if hashmap[char] == 2:
                return char