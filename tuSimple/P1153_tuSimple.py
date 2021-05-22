class Solution:
    def canConvert(self, str1: str, str2: str) -> bool:
        in_degree = defaultdict(int)
        edges = defaultdict(str)
        for a, b in zip(str1, str2):           
            if a in edges:
                if edges[a]!=b:
                    return False
            else:
                edges[a] = b
                in_degree[b] += 1

        q = [k for k in edges if in_degree[k] == 0]
        for a in q:
            in_degree[edges[a]] -= 1
            if in_degree[edges[a]] == 0:
                q.append(edges[a])
                
        n_cycles = 0
        visited = set(q)
        for c in set(str1):
            if c not in visited:                
                if edges[c] != c:
                    n_cycles += 1                    
                    cc = c
                    while cc not in visited:
                        visited.add(cc)
                        cc = edges[cc]

        return n_cycles <= 26 - len(set(str2))
        