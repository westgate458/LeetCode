class Solution(object):
    def findBuildings(self, heights):
        """
        :type heights: List[int]
        :rtype: List[int]
        """                      
        res, cur_max = [], 0         
        for i in range(len(heights)-1,-1,-1):            
            if heights[i] > cur_max:
                res.append(i)
                cur_max = heights[i]            
        return res[::-1]