class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        res = list(s)
        ss = []
        for p, c in enumerate(s):
            if c == ')':
                if not ss:
                    res[p] = '*'
                else:
                    ss.pop()
            elif c == '(':
                ss.append(p)            
        for p in ss:
            res[p] = '*'
        return(''.join(res).replace('*',''))