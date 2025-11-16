class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closedtoopen = {")":"(", "}":"{", "]":"["}

        for char in s:
            if char in closedtoopen:
                if stack and stack[-1] == closedtoopen[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        
        if len(stack) == 0:
            return True
        else:
            return False
    
  
