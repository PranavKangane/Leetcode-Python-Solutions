class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)

        for words in strs:
            key = "".join(sorted(words))
            hashmap[key].append(words)

        return list(hashmap.values()) 
        