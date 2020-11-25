class Solution(object):
    def findRedundantDirectedConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        # start DFS from node of in-degree of 0, or node of max out-degree
        N = len(edges)+1        
        in_degree, ou_degree, visited = [0]*N, [0]*N, [0]*N 
        adj = defaultdict(list)        
        
        for i, (u, v) in enumerate(edges):
            adj[u].append((v,i))
            in_degree[v] += 1
            ou_degree[u] += 1            
        
        in_2_node = root = in_2_id = -1
        for u, i in enumerate(in_degree[1:],1):
            if i == 0: root = u
            elif i == 2: in_2_node = u
                
        if root == -1:
            ou_max = -1
            for i, o in enumerate(ou_degree):
                if o > ou_max: ou_max, root = o, i
        
        q = [root]
        while q:
            u = q.pop()
            if visited[u] == 0:
                visited[u] = 1 
                q.append(u)
                for v, i in adj[u]:   
                    if (v == in_2_node) and (i > in_2_id): in_2_id = i
                    if visited[v] == 1: return edges[i]                              
                    elif visited[v] == 0: q.append(v)        
            else:
                visited[u] = 2 
        return edges[in_2_id]
    
  