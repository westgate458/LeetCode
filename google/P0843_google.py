# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Master(object):
#    def guess(self, word):
#        """
#        :type word: str
#        :rtype int
#        """

class Solution(object):
    def findSecretWord(self, wordlist, master):
        """
        :type wordlist: List[Str]
        :type master: Master
        :rtype: None
        """         
        while True:            
            word = random.choice(wordlist)         
            res = master.guess(word)            
            if res == 6: return            
            wordlist = [w for w in wordlist if sum([i==j for i, j in zip(w,word)])==res]            
        return
                
            
                    
                    
            