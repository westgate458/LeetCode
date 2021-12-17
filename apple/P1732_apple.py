class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        res = s = 0        
        for g in gain:
            s += g
            if s > res: res = s
        return res