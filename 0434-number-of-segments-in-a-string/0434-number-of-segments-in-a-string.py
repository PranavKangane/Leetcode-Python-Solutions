class Solution:
    def countSegments(self, s: str) -> int:
        
        if len(s.strip()) == 0:
            return 0
        else:
            list1 = s.strip().split()

            return len(list1)
        