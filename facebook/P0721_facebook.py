class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        
        names = defaultdict()
        edges = defaultdict(list)  
        
        for account in accounts:    
            names[account[1]] = account[0]
            for i in range(1, len(account)-1):
                edges[account[i]].append(account[i+1])
                edges[account[i+1]].append(account[i]) 
                names[account[i+1]] = account[0]
        
        res = []                
        
        for node in names.keys():
            if names[node] != '':    
                name = names[node]
                names[node] = ''
                q = [node]
                for n in q:
                    for nn in edges[n]:
                        if names[nn] != '':
                            q.append(nn)
                            names[nn] = ''                                 
                res.append([name]+sorted(q))        
        return res
            
            