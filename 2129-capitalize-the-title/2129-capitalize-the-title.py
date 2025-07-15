class Solution:
    def capitalizeTitle(self, title: str) -> str:
        
        str = ""

        list1 = list(title.split())
        for i in list1:
            if len(i) < 3:
                str += i.lower()
                str += " "
            else:
                str += i.capitalize()
                str += " "


        return str.rstrip()


        
