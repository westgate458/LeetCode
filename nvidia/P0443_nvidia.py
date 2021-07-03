class Solution:
    def compress(self, chars: List[str]) -> int:
        p, res, ll = 0, 0, len(chars)
        for pp in range(ll+1):
            if pp == ll or chars[pp] != chars[p]:
                l = pp - p  
                if l == 1:     
                    ch = [chars[p]]                
                else:
                    ch = [chars[p]]+list(str(l))                
                chars[res:res+len(ch)] = ch
                p = pp      
                res += len(ch)         
        return res