class Solution(object):
    def outerTrees(self, points):
        """
        :type points: List[List[int]]
        :rtype: List[List[int]]
        """
		# convex hull
        if len(points) <= 3: return points
        
        points.sort(key=lambda p:(p[1], -p[0]))
        
        x0, y0 = points[0]
        points.pop(0)
        
        pos_dx, neg_dx, zer_dx, zer_dy = [], [], [], []
        
        for x, y in points:
            if y == y0:
                zer_dy.append([x, y])                
            elif x > x0:
                pos_dx.append([x, y])
            elif x < x0:
                neg_dx.append([x, y])
            else:
                zer_dx.append([x, y])
        
        points = []
        if pos_dx:
            points += sorted(pos_dx, key=lambda (x,y):(float(y-y0)/(x-x0), (y-y0)**2+(x-x0)**2))
        if zer_dx:
            points += sorted(zer_dx, key=lambda (x,y):((y-y0)**2+(x-x0)**2)) 
        if points:
            points += sorted(neg_dx, key=lambda (x,y):(float(y-y0)/(x-x0), -(y-y0)**2-(x-x0)**2))     
        else:
            points += sorted(neg_dx, key=lambda (x,y):(float(y-y0)/(x-x0), (y-y0)**2+(x-x0)**2))  
        if zer_dy:
            points += sorted(zer_dy, key=lambda (x,y):(-(y-y0)**2-(x-x0)**2))
        
        res = [[x0,y0],points[0]]          
        for x3, y3 in points[1:]: 
            while (res[-2][0] - res[-1][0])*(y3 - res[-1][1]) - (res[-2][1] - res[-1][1])*(x3 - res[-1][0]) > 0: res.pop()
            res.append([x3, y3]) 
        return(res)