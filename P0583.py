class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
		# build from short to long
        l1, l2 = len(word1), len(word2)
        
        d = [[0] * (l2+1) for _ in range(l1+1)]
        
        for i in range(1,l1+1): d[i][0] = i
        for j in range(1,l2+1): d[0][j] = j
        
        for i in range(1,l1+1):
            for j in range(1,l2+1):
                d[i][j] = min(d[i-1][j-1] if word1[i-1] == word2[j-1] else d[i-1][j-1] + 2, d[i-1][j] + 1, d[i][j-1] + 1)
                   
        return(d[-1][-1])
        
        
        