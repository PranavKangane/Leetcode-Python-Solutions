class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        list1 = s.strip().split(" ")
        last = len(list1)
        lastword = list1[last-1]
        length = len(lastword)
        return length