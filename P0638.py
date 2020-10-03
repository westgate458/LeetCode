class Solution(object):
    def shoppingOffers(self, price, special, needs):
        """
        :type price: List[int]
        :type special: List[List[int]]
        :type needs: List[int]
        :rtype: int
        """
		# DFS with restrictions
        self.res = float('inf')
        def DFS(cost, needs):            
            if sum(needs) != 0:  
                self.res = min(self.res, cost + sum([p*n for p, n in zip(price, needs)]))
                for offer in special:
                    pairs = zip(offer[:-1], needs)
                    if all([o<=n for o, n in pairs]) and (cost+offer[-1] < self.res):
                        DFS(cost+offer[-1], [n-o for o, n in pairs])   
            else:
                self.res = min(cost, self.res)
        DFS(0, needs)
        return self.res 