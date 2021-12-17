class Solution(object):
    def longestStrChain(self, words):
        """
        :type words: List[str]
        :rtype: int
        """       
        dp = defaultdict(int)
        
        def check(w1,w2):            
            k = 0
            while k < len(w1) and w1[k]==w2[k]: k += 1
            return w1[k:]==w2[k+1:]        
        
        words_by_len = defaultdict(list)
        for word in words:
            words_by_len[len(word)].append(word)

        for l in sorted(words_by_len.keys(),reverse=True):
            for w1 in words_by_len[l]:
                for w2 in words_by_len[l+1]:                    
                    if check(w1,w2) and dp[w2]+1>dp[w1]:
                        dp[w1] = dp[w2]+1             
        
        return max(dp.values())+1 if dp else 1        