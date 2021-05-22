class Solution:
    def calculate(self, s: str) -> int:          
        t = ['(']     
        n = ''
        for c in s+')':            
            if c in "0123456789":
                n += c
            else:        
                if c == '(':
                    if n == '-': t += [-1,'*'] 
                    t += ['('] 
                else:
                    if n: t += [int(n)]
                    if t[-2] == '*': 
                        t[-3] = t[-3] * t[-1]
                        t.pop()
                        t.pop() 
                    elif t[-2] == '/': 
                        if t[-3] > 0: t[-3] = t[-3] // t[-1]                        
                        else: t[-3] = -((-t[-3]) // t[-1]) 
                        t.pop()
                        t.pop()                         
                    if c in '*/': t += [c]    
                if c == '-': 
                    n = '-'
                else: 
                    n = ''                    
                if c == ')':
                    num = 0
                    while t[-1] != '(': num += t.pop()                         
                    t[-1] = num
        return(t[0])