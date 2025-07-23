class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        total = 0
        i = 0
        while i < len(operations):
            if operations[i] == '--X' or operations[i] == 'X--':
                total -= 1
                i += 1
            elif operations[i] == '++X' or operations[i] == 'X++':
                total += 1
                i += 1

        return total