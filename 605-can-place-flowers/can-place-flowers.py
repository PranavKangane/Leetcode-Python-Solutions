class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
            i = 0
            while i < len(flowerbed):
                if flowerbed[i] == 1:
                    i += 1
                else:
                    left_empty = (i == 0) or (flowerbed[i-1] == 0)
                    right_empty = (i == len(flowerbed)-1) or (flowerbed[i+1] == 0)

                    if left_empty and right_empty:
                        flowerbed[i] = 1
                        n -= 1

                        if n == 0:
                            return True

                        i += 2  # skip next spot
                    else:
                        i += 1

            return n <= 0

        