import heapq
class Solution(object):
    def findMaximizedCapital(self, k, W, Profits, Capital):
        """
        :type k: int
        :type W: int
        :type Profits: List[int]
        :type Capital: List[int]
        :rtype: int
        """       
		# Solution 1 beats 100%: heap
        if W >= max(Capital):
            return W+sum(sorted(Profits,reverse=True)[:k])  
        t = sorted(zip(Capital, Profits),reverse=True) 
        heap = []        
        for _ in range(k):            
            while t and t[-1][0] <= W: heapq.heappush(heap, - t.pop()[1])                          
            if heap: W -= heapq.heappop(heap) 
            else: break               
        return(W)
		# Solution 2 beats 12.5%: naive loops
		t = sorted(zip(Profits, Capital), reverse=True)
        Profits = [p[0] for p in t]
        Capital = [p[1] for p in t]
        k = min(k, len(Profits))        
        flag = True
        while k > 0 and flag: 
            flag = False
            for i, c in enumerate(Capital):
                if c <= W:
                    W += Profits[i]
                    Profits.pop(i)
                    Capital.pop(i)
                    k -= 1
                    flag = True
                    break                    
        return(W)