class Solution:
    def alienOrder(self, words: List[str]) -> str:
        
        if len(words) == 1: return words[0]
        
        in_degree = {a:0 for a in set(''.join(words))}
        
        edges = defaultdict(set)
        
        ls = list(map(len,words))
        for i in range(len(words)-1):
            if ls[i+1]<ls[i]:
                if words[i][:ls[i+1]] == words[i+1]:            
                    return ""
            for a, b in zip(words[i],words[i+1]): 
                if a != b:                     
                    if a in edges[b]:
                        return ""                        
                    if b not in edges[a]:
                        in_degree[b] += 1
                        edges[a].add(b)
                    break                         
        
        q = [k for k, v in in_degree.items() if v == 0]   
        for a in q:
            in_degree[a] = -1
            for b in edges[a]:
                if in_degree[b] == -1:
                    return ""
                else:
                    in_degree[b] -= 1
                    if in_degree[b] == 0:
                        q.append(b)        
        
        return ''.join(q) if len(q) == len(in_degree) else ""            