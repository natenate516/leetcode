class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        vaild = 0
        flowerbed = [0] + flowerbed + [0]

        for i in range(1, len(flowerbed) - 1):
            if flowerbed[i-1] == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0:
                flowerbed[i] = 1
                vaild += 1
            
        return n <= vaild
        