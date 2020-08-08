class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """   
		# BFS from seeds
        q, m, n = [], len(matrix), len(matrix[0])
        for r, row in enumerate(matrix):
            for c, cell in enumerate(row):
                if cell == 0: q.append((r,c,0))
                else: matrix[r][c] = -1        
        for r, c, d in q:        
            for rr, cc in [(r-1,c),(r+1,c),(r,c-1),(r,c+1)]:
                if (0 <= rr < m) and (0 <= cc < n) and (matrix[rr][cc] == -1):
                    matrix[rr][cc] = d + 1
                    q.append((rr,cc,d+1))
        return matrix