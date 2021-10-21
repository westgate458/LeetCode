class Solution(object):
    def findAllConcatenatedWordsInADict(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """        
        def isCat(w):
            if not w: return False
            dp = [False] * (len(w)+1)
            dp[0] = True
            for i in range(1,len(w)+1):
                for j in range(i):
                    if dp[j] and (w[j:i] in preWords):
                        dp[i] = True
                        break
            return dp[-1]
        res = []
        preWords = set()
        for w in sorted(words,key=len):
            if isCat(w):
                res.append(w)
            preWords.add(w)
            
        return res
        