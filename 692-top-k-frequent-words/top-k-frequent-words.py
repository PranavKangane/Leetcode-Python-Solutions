class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        hashmap = {}
        for i in words:
            hashmap[i] = hashmap.get(i,0) + 1

        freq = [[] for i in range(len(words)+1)]
        for i, v in hashmap.items():
            freq[v].append(i)

        for sublist in freq:
            sublist.sort()
        
        final = []
        for i in range(len(freq)-1,-1,-1):
            for word in freq[i]:
                final.append(word)
                if len(final) == k:
                    return final
