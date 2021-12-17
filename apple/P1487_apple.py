class Solution(object):
    def getFolderNames(self, names):
        """
        :type names: List[str]
        :rtype: List[str]
        """
        res = []
        d = defaultdict(int)
        for n in names:
            nn = n
            while nn in d:
                d[n] += 1 
                nn = n + '(%d)'%d[n]  
            d[nn] = 0
            res.append(nn)
        return res