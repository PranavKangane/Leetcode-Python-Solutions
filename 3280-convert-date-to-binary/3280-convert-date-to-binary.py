class Solution:
    def convertDateToBinary(self, date: str) -> str:
        yearpart =  str(bin(int(date[:4])))[2:]
        monthpart = str(bin(int(date[5:7])))[2:]
        daypart = str(bin(int(date[8:])))[2:]
        final = (f"{yearpart}-{monthpart}-{daypart}")
        return final
     

       