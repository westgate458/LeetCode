class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        def check(word, pattern):
            m, n = {}, {}            
            for a, b in zip(word,pattern):
                if ((a in m) and (m[a]!=b)) or ((b in n) and (n[b]!=a)):
                    return False
                else:
                    m[a], n[b] = b, a                    
            return True      
        return [word for word in words if check(word, pattern)]