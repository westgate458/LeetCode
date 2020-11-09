class Solution(object):
    def cutOffTree(self, forest):
        """
        :type forest: List[List[int]]
        :rtype: int
        """
		# min heap for seeding order, BFS for shortest path
        def BFS(x0, y0, x1, y1, id):
            if (x0==x1) and (y0==y1): return 0
            q, forest[x0][y0] = deque([(x0,y0,0)]), id
            while q:
                x, y, ss = q.popleft()
                for xx, yy in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
                    if (0<=xx<m) and (0<=yy<n) and (forest[xx][yy]!=0 and forest[xx][yy]!=id):
                        if (xx==x1) and (yy==y1): return ss+1
                        q.append((xx,yy,ss+1))                        
                        forest[xx][yy] = id
            return -1
        
        m, n, x0, y0, id, res = len(forest), len(forest[0]), 0, 0, 0, 0     
        for _, x, y in sorted([(forest[i][j], i, j) for i in range(m) for j in range(n) if forest[i][j] > 1]) :
            id -= 1
            s = BFS(x0, y0, x, y, id)
            if s == -1: return -1
            else:
                res, x0, y0 = res+s, x, y               
        return res