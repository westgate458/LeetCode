class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        
        m, n = len(picture), len(picture[0])
        t1 = [0]*m
        t2 = [0]*n            
        for i in range(m):
            for j in range(n):
                if picture[i][j] == 'B':
                    t1[i] += 1
                    t2[j] += 1            
        res = 0
        for i in range(m):
            if t1[i] == 1:
                for j in range(n):
                    if picture[i][j] == 'B' and t2[j] == 1:
                        res += 1                
        return res
                              
        