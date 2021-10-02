class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        
        m, k, n = len(mat1), len(mat1[0]), len(mat2[0])        
        
        mat1_d = [[] for _ in range(k)]
        mat2_d = [[] for _ in range(k)]
        res = [[0]*n for _ in range(m)]
        
        for kk in range(k):        
            for i in range(m):            
                if mat1[i][kk]:
                    mat1_d[kk].append(i)        
            for j in range(n):            
                if mat2[kk][j]:
                    mat2_d[kk].append(j)
        
        for kk in range(k):
            for i in mat1_d[kk]:
                for j in mat2_d[kk]:
                    res[i][j] += mat1[i][kk] * mat2[kk][j]                            
        
        return res
        