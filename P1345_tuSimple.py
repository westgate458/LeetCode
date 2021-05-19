class Solution:
    def minJumps(self, arr: List[int]) -> int:
        
        l = len(arr)
        if l == 1: return(0)
        if l == 2 or arr[0] == arr[-1]: return(1)
        if l == 3 or arr[0] == arr[-2] or arr[1] == arr[-1]: return(2)       
        
        arr_new = [arr[0]]
       
        for i in range(1,l):
            if arr[i-1] == arr[i] == arr[i+1]:
                pass
            else:
                arr_new.append(arr[i])
        
        arr = arr_new   
                   
        vals = {}
        edges = {}
        for i, num in enumerate(arr):  
            edges[i] = []
            if i-1 >= 0:
                edges[i].append(i-1)
            if i+1 < len(arr):
                edges[i].append(i+1)            
            if num in vals:
                for j in vals[num]:
                    edges[i].append(j)
                    edges[j].append(i)
                vals[num].append(i)
            else:
                vals[num] = [i]

        visited = set([0])
        q = [(0,0)]        
        for i, step in q:
            for j in edges[i]:
                if j == len(arr)-1:
                    return(step+1)
                if j not in visited:
                    q.append((j,step+1))
                    visited.add(j)
        return(0)