class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        l = len(isConnected)
        roots = [i for i in range(l)]        
        def findRoot(n):
            if roots[n] == n:
                return n
            else:
                r = findRoot(roots[n])
                roots[n] = r
                return r        
        for i in range(l):
            for j in range(i+1,l):
                if isConnected[i][j]:                   
                    roots[findRoot(i)] = findRoot(j)        
        res = set()
        for i in range(l):            
            res.add(findRoot(i))        
        return len(res)