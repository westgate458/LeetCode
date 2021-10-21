class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:        
        def calOrders(level):
            order = 0
            for j in inventory:
                if j >= level:                   
                    n = j - level + 1
                    order += n                    
                else:
                    break
            return order
        
        inventory.sort(reverse=True)
                
        l, r = 1, inventory[0] 
        while l < r:
            m = (l+r)//2            
            if calOrders(m) >= orders: l = m + 1
            else: r = m - 1
                
        while calOrders(l) <= orders: l -= 1  
        l = l + 1
                
        res = 0        
        for j in inventory:            
            if j >= l:                                                
                n = j-l+1                
                orders -= n             
                res += (l+j)*n//2                   
            else:
                break
        return (res + orders*(l-1))%(10**9+7)