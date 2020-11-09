class MagicDictionary(object):
	# using Trie, try changing each character during searching the word
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = {}
        self.isWord = True

    def buildDict(self, dictionary):
        """
        :type dictionary: List[str]
        :rtype: None
        """
        for word in dictionary:
            node = self.d
            for c in word:
                if c not in node:                
                    node[c] = {}              
                node = node[c]
            node[self.isWord] = True        
        
    def DFS(self, node, word, changed):        
        if word == '':
            return changed and (self.isWord in node) 
        else:
            if (word[0] in node) and self.DFS(node[word[0]], word[1:], changed):
                return True                 
            elif not changed:         
                for n in node:
                    if (n!=self.isWord) and (word[0]!= n) and self.DFS(node[n], word[1:], True):                    
                        return True
            return False
                    
    
    def search(self, searchWord):
        """
        :type searchWord: str
        :rtype: bool
        """
        return self.DFS(self.d, searchWord, False)


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)