class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        prev, anex, count = 0, 0, 0
        for i in range(0, len(flowerbed)):
            if flowerbed[i]==0:
                prev = 0 if i==0 else flowerbed[i-1]
                anex = 0 if i==len(flowerbed)-1 else flowerbed[i+1]
                if prev==0 and anex==0:
                    flowerbed[i]=1
                    count = count+1
        return count>=n