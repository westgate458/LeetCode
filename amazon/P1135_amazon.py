class Solution(object):
    def minimumCost(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        
        def findRoot(r):
            if roots[r] != r:
                roots[r] = findRoot(roots[r])
            return roots[r]
                
        res = 0
        roots = [i for i in range(n+1)]
        for a, b, c in sorted(connections, key = lambda x:x[2]):            
            r_a = findRoot(a)
            r_b = findRoot(b)
            if r_a != r_b:
                roots[r_a] = r_b
                res += c
        
        n_roots = set()
        for i in range(1,n+1):
            n_roots.add(findRoot(i))
            
        if len(n_roots) == 1:
            return res
        else:
            return -1