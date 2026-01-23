class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        string = int(''.join(list(map(str,digits))))+1
        result = [int(i) for i in str(string)]
        return result

       
       