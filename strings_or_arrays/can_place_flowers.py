# https://leetcode.com/problems/can-place-flowers/
class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        for i in range(len(flowerbed)):
            if n == 0:
                return True
            if flowerbed[i] == 1:
                continue
            left = flowerbed[i-1] if i > 0 else 0
            right = flowerbed[i+1] if i < len(flowerbed) - 1 else 0

            if left == 0 and right == 0:
                flowerbed[i] = 1
                n = n - 1

        return n == 0
