class Solution(object):
    def numMatchingSubseq(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: int
        """
        # Solution 1: bisect
        h = defaultdict(list)
        for i, c in enumerate(s): h[c] += [i]            
        def is_sub(word):
            last = -1
            for c in word:                
                i = bisect.bisect_right(h[c], last)                
                if (i == len(h[c])) or (h[c][i]==last): return False
                else: last = h[c][i]                    
            return True        
        return sum([is_sub(word) for word in words])
        
        # Solution 2: built-in find 
        def is_sub(word):
            i = 0
            for c in word:                
                j = s.find(c,i)               
                if j == -1: return False
                else: i = j+1               
            return True 
        return sum([c for w,c in Counter(words).items() if is_sub(w)])