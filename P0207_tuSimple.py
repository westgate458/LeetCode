class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        in_degree = [0]*numCourses
        edges = defaultdict(list)
        for a,b in prerequisites:
            in_degree[b] += 1            
            edges[a] += [b]        
        inds = [i for i,d in enumerate(in_degree) if d==0]
        for i in inds:
            for j in edges[i]:
                in_degree[j] -= 1
                if in_degree[j] == 0:
                    inds.append(j)                    
        for d in in_degree:
            if d != 0:
                return False
        return True