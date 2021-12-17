class Solution(object):
    def getBiggestThree(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        m, n = len(grid), len(grid[0])
        l = min(m,n)//2+1
        r1 = r2 = r3 = 0
        for ll in range(l):                   
            for i in range(ll,m-ll):
                for j in range(ll,n-ll): 
                    if ll == 0:
                        s = grid[i][j]
                    else:
                        s = grid[i-ll][j]+grid[i+ll][j]+grid[i][j+ll]+grid[i][j-ll]
                        for di in range(1,ll):
                            dj = ll-di
                            s += grid[i+di][j+dj]+grid[i+di][j-dj]+grid[i-di][j+dj]+grid[i-di][j-dj]                        
                    if s > r1:
                        if s > r2:
                            if s > r3:
                                r3, r2, r1 = s, r3, r2
                            elif s != r3:
                                r2, r1 = s, r2
                        elif s != r2:
                            r1 = s                    
        
        if r1 == r2 == 0: return [r3]
        if r1 == 0: return [r3, r2]
        return [r3,r2,r1]