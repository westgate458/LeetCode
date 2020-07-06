class Solution(object):
    def findRotateSteps(self, ring, key):
        """
        :type ring: str
        :type key: str
        :rtype: int
        """        
		# Solution 1 beats 87.04%: straight DP
        self.ps, l_ring, dp = defaultdict(list), len(ring), [(0,0)]
        for p, r in enumerate(ring): self.ps[r].append(p)
        for c in key: dp = [(p,min([min(cost+abs(pos-p),cost+l_ring-abs(pos-p)) for pos, cost in dp])+1) for p in self.ps[c]]           
        return(min([c for _,c in dp]))
		
		# Solution 2 beats 27.78%: DPS + memorization
		self.d = {}        
        self.ps = defaultdict(list)
        for p, r in enumerate(ring): self.ps[r].append(p) 
        l_key = len(key)
        l_ring = len(ring)        
        def DFS(pos, k): 
            if k == l_key : return 0
            if (pos, k) in self.d: return self.d[(pos, k)] 
            self.d[(pos, k)] = float('inf')
            for p in self.ps[key[k]]:
                self.d[(pos, k)] = min(self.d[(pos, k)], min(DFS(p, k+1)+ abs(pos-p),DFS(p, k+1)+ l_ring - abs(pos-p))) 
            self.d[(pos, k)] += 1
            return(self.d[(pos, k)])      
        return(DFS(0,0))
		