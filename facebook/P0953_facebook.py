class Solution:    
    def isAlienSorted(self, words: List[str], order: str) -> bool:        
        o = {c:i for i, c in enumerate(order)}         
        for i in range(len(words)-1):    
            if len(words[i]) > len(words[i+1]) and words[i][:len(words[i+1])] == words[i+1]: return False            
            for a,b in zip(words[i],words[i+1]):                
                if a == b: continue
                elif o[a] < o[b]: break
                elif o[a] > o[b]: return False
        return True