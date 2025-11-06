class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rmap = {}
        mmap = {}

        for x in range(len(ransomNote)):
            rmap[ransomNote[x]] = rmap.get(ransomNote[x],0)+1

        for x in range(len(magazine)):
            mmap[magazine[x]] = mmap.get(magazine[x],0)+1

        print(rmap)
        print(mmap)

        for index1,value1 in rmap.items():
            if index1 not in mmap:
                return False
            elif index1 in mmap:
                if value1 <= mmap.get(index1,0):
                    continue
                else:
                    return False

        return True



