class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        numout = [0 for x in range(len(temperatures))]
        stack = []
        indices = []


        for i in range(len(temperatures)-1,-1,-1):
            while stack and stack[-1] <= temperatures[i]:
                stack.pop()
                indices.pop()

            if not stack:
                numout[i] = 0
            else:
                ind = indices[-1]- i
                numout[i] = ind
            
            stack.append(temperatures[i])
            indices.append(i)

        return numout


        