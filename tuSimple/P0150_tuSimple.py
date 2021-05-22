class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        for t in tokens:
            if t in "+-*/":
                b = s.pop()
                a = s.pop()
                if t == '+':
                    s.append(a+b)
                elif t == '-':
                    s.append(a-b)
                elif t == '*':
                    s.append(a*b)
                elif t == '/':
                    if (a*b)>0:
                        s.append(a//b)
                    else:
                        s.append(-((-a)//b))
            else:
                s.append(int(t))
        return(s[0])