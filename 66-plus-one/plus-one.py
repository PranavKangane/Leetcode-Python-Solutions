class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
       data = str(int("".join(list(map(str,digits))))+1)
       newstr = list(map(int,data))
       return newstr
       
       
       