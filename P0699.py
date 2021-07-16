class Solution(object):
    def fallingSquares(self, positions):
        """
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        ls = [0,10**9]
        rs = [0,10**9]
        hs = [0,0]        
        res = [0]        
        for a, h in positions:                
            b = a + h            
            i = bisect.bisect_left(ls, a)            
            if (a >= rs[i-1] and b <= ls[i]):
                ls = ls[:i] + [a] + ls[i:]
                rs = rs[:i] + [b] + rs[i:]
                hs = hs[:i] + [h] + hs[i:]
            else:
                h_max = 0
                if a < rs[i-1]: i -= 1
                j = i
                while j < len(rs) and b > ls[j]:
                    h_max = max(h_max, hs[j])                    
                    j += 1    
                j -= 1
                c, d, h = ls[i], rs[j], h_max+h
                if c < b < d:
                    if a <= c:                        
                        ls = ls[:i] + [a,b] + ls[j+1:] 
                        rs = rs[:i] + [b,d] + rs[j+1:]
                        hs = hs[:i] + [h,hs[j]] + hs[j+1:]
                    elif a > c:  
                        ls = ls[:i] + [c,a,b] + ls[j+1:] 
                        rs = rs[:i] + [a,b,d] + rs[j+1:]
                        hs = hs[:i] + [hs[i],h,hs[j]] + hs[j+1:]                        
                elif b >= d:
                    if a <= c:                        
                        ls = ls[:i] + [a] + ls[j+1:] 
                        rs = rs[:i] + [b] + rs[j+1:]
                        hs = hs[:i] + [h] + hs[j+1:]
                    elif a > c:                        
                        ls = ls[:i] + [c,a] + ls[j+1:] 
                        rs = rs[:i] + [a,b] + rs[j+1:]
                        hs = hs[:i] + [hs[i],h] + hs[j+1:]            
            if h >= res[-1]: res.append(h)
            else: res.append(res[-1])        
        return res[1:]