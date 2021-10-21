class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        r = 0        
        for i, j in sorted(boxTypes, key=lambda x:-x[1]):
            n = min(truckSize, i)
            r += n*j
            truckSize -= n
            if truckSize <=0: break
        return r
        