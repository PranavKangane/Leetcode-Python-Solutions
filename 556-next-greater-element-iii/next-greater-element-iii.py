class Solution:
    def nextGreaterElement(self, n: int) -> int:
        nlist = [int(x) for x in str(n)]
        right = len(nlist) - 2
        l = len(nlist)

        while right >= 0 and nlist[right] >= nlist[right + 1]:
            right -= 1

        if right < 0:
            return -1

        pivot_digit = nlist[right]

        swapdigit = -1
        smallest = float('inf')
        for i in range(right + 1, l):
            if nlist[i] > pivot_digit and nlist[i] < smallest:
                smallest = nlist[i]
                swapdigit = i

        nlist[right], nlist[swapdigit] = nlist[swapdigit], nlist[right]

        nlist[right + 1:] = sorted(nlist[right + 1:])

        newnum = int("".join(map(str, nlist)))

        return newnum if newnum < 2**31 else -1