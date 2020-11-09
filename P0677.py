class MapSum(object):
	# using Trie, find all words starting with a prefix by BFS 
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = {}        

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: None
        """
        node = self.d
        for c in key:
            if c not in node:                
                node[c] = {}              
            node = node[c]
        node['val'] = val
        

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        node = self.d
        for c in prefix:
            if c not in node:                
                return 0
            node = node[c]       
        q = [node]
        res = 0
        while q:
            node = q.pop()
            for n in node:
                if n == 'val':
                    res += node['val']
                else:
                    q.append(node[n])
        return res