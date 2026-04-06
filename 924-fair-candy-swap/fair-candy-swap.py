class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        aCount = 0
        bCount = 0
        for candy in aliceSizes:
            aCount += candy
        for candy in bobSizes:
            bCount += candy
        
        dif = (aCount - bCount) / 2

        aliceSet = set(aliceSizes)
        for candy in bobSizes:
            if dif + candy in aliceSet:
                return [dif + candy, candy]
        return -1
        
