class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if endWord not in wordList: return 0 
        adj = defaultdict(list)
        l = len(wordList[0])
        for word in wordList: 
            for j in range(l):
                adj[word[:j]+'*'+word[j+1:]].append(word)  
        q = [(beginWord,1)]  
        available = set(wordList)
        for word, s in q:            
            for j in range(l):                        
                for ww in adj[word[:j]+'*'+word[j+1:]]:     
                    if ww == endWord: return s+1
                    if ww in available:                    
                        q.append((ww, s+1))
                        available.remove(ww)
        return 0
            
            