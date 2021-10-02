class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        def compare(s1,s2):
            if s1==s2: return True            
            mismatch = 0
            for c1,c2 in zip(s1,s2):
                if c1==c2: continue
                mismatch += 1
                if mismatch==1:
                    p1 = c1
                    p2 = c2
                elif mismatch==2:                    
                    if (c1!=p2) or (c2!=p1): return False
                else:
                    return False
            return True
        
        m = defaultdict(set)
        
        l = len(strs)
        for i in range(l):
            for j in range(i+1,l):                
                if compare(strs[i],strs[j]):
                    m[strs[i]].add(strs[j])
                    m[strs[j]].add(strs[i])
                
        visited = set()
        res = 0
        for s in strs:
            if s not in visited:
                res += 1
                visited.add(s)
                q = [s]
                for n in q:
                    for ss in m[n]:
                        if ss not in visited:
                            visited.add(ss)
                            q += [ss]
                    
        return(res)