class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """ 
        
        # Solution 0: cheat by sorting
        return(map(int,sorted(map(str,range(1,n+1)))))     
        
        # Solution 1: build Trie first, then DFS
        trie = OrderedDict()        
        for i in range(1,n+1):
            s = str(i)
            node = trie
            for c in s:
                if c in node:
                    node = node[c]
                else:
                    node[c] = OrderedDict()
                    node = node[c]
            node['is_leaf'] = s                
        res = []        
        def DFS(node):
            if 'is_leaf' in node:
                res.append(node['is_leaf'])
            for n in node:
                if n != 'is_leaf':
                    DFS(node[n])             
        DFS(trie)
        return res
        
        # Solution 2: direct DFS
        def DFS(i):
            return [i] + [jj for j in range(i*10,i*10+10) if 0 < j <= n for jj in DFS(j)]        
        return DFS(0)[1:]