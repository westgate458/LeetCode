class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        
        def merge(buildings):
            l = len(buildings)
            if l == 1: return([[buildings[0][0],buildings[0][2]],[buildings[0][1],0]])
            
            res_1, res_2 = merge(buildings[:l//2]), merge(buildings[l//2:])                    
            
            h_1 = h_2 = i = j = 0 
            res = []
            h_pre = -1
            while i < len(res_1) and j < len(res_2):
                               
                x = min(res_1[i][0],res_2[j][0])
                
                if res_1[i][0] == x:
                    h_1 = res_1[i][1]
                    i += 1
                if res_2[j][0] == x:
                    h_2 = res_2[j][1]
                    j += 1
                
                h = max(h_1,h_2)
                if h != h_pre:               
                    res.append([x,h])
                    h_pre = h
                
            if i < len(res_1): res += res_1[i:]
            if j < len(res_2): res += res_2[j:]
            
            return res
            
        return(merge(buildings))