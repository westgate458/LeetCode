class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """        
		# DFS to find circle
        adj = defaultdict(list)
        ids = {}
        for i, (u, v) in enumerate(edges):
            adj[u].append((v,i))
            adj[v].append((u,i))
            ids[(u,v)] = i
            ids[(v,u)] = i
        def DFS(u, path, path_ids):
            for v, i in adj[u]:
                if (v==path[-1]): continue                    
                if (v in set(path)): return max(path_ids[path.index(v):]+[ ids[(u,v)], ids[(u,path[-1])]])
                else:
                    id = DFS(v, path+[u], path_ids+[i])
                    if id != -1: return id
            return -1
        id = DFS(1, [-1], [-1])        
        return edges[id]