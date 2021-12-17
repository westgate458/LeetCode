class Trie(object):

    def __init__(self):
        
        self.d = {}        

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """        
        node = self.d        
        for c in word:
            if c not in node: node[c] = {}
            node = node[c]
            if '@' not in node: node['@'] = 0
            node['@'] += 1            
        if '*' not in node: node['*'] = 0
        node['*'] += 1        

    def countWordsEqualTo(self, word):
        """
        :type word: str
        :rtype: int
        """        
        node = self.d        
        for c in word:
            if c not in node: return 0
            node = node[c]        
        return node.get('*', 0)        

    def countWordsStartingWith(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        node = self.d        
        for c in prefix:
            if c not in node: return 0
            node = node[c]        
        return node.get('@', 0)
            
    def erase(self, word):
        """
        :type word: str
        :rtype: None
        """        
        node = self.d        
        for c in word:
            if c not in node: return 
            node = node[c]
            node['@'] -= 1            
        if '*' in node: node['*'] -= 1

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.countWordsEqualTo(word)
# param_3 = obj.countWordsStartingWith(prefix)
# obj.erase(word)