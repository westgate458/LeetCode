class Solution:
    def countOfAtoms(self, formula: str) -> str:        
        def helper(s):            
            d = defaultdict(int)
            i = 0            
            preC = '#'    
            preK = 0            
            while i < len(s):                 
                if s[i].isalpha():                    
                    if s[i].isupper():
                        if preK == 0:
                            preK = 1
                        d[preC] += preK
                        preC = s[i]
                        preK = 0
                    else:
                        preC += s[i]
                    i += 1
                elif s[i].isdigit():
                    preK = preK*10+int(s[i])
                    i += 1
                else:
                    j = i+1
                    c = 1
                    while c != 0:                        
                        if (s[j] == '('): c += 1
                        elif (s[j] == ')'): c -= 1                          
                        j += 1
                    dd = helper(s[i+1:j-1])                    
                    if (j==len(s)) or (s[j].isalpha()) or (s[j]=='('):
                        m = 1
                        i = j
                    else:
                        k = j+1
                        while (k < len(s)) and (s[k].isdigit()):
                            k += 1
                        m = int(s[j:k])
                        i = k                    
                    for key in dd:                        
                        d[key] += dd[key]*m 
            if preK == 0:
                preK = 1
            d[preC] += preK 
            return(d)
        
        d = helper(formula)
        res = ''
        for key in sorted(d.keys())[1:]:   
            res = res + key
            if d[key] != 1:
                res = res + str(d[key])
        return(res)