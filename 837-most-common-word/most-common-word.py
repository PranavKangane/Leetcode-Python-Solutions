class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        mapping = str.maketrans("!?',;.","      ")
        para = paragraph.translate(mapping)
        newp = para.split()
        para2 = [x.lower() for x in newp]

        hashmap = {}
        for x in para2:
            hashmap[x] = hashmap.get(x,0) + 1

        for ban in banned:
            if ban in hashmap:
                hashmap.pop(ban)

        freq = [[] for x in range(len(para2)+1)]
        for index, value in hashmap.items():
            freq[value].append(index)

        for words in reversed(freq):
            if words:
                return "".join(words)
            

        