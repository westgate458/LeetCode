class Solution:
    def isValid(self, s: str) -> bool:
        t = ['*']
        for c in s:
            if c in "([{":
                t.append(c)
            elif c == ')':
                if t[-1] == '(': t.pop()
                else: return False
            elif c == ']':
                if t[-1] == '[': t.pop()
                else: return False
            elif c == '}':
                if t[-1] == '{': t.pop()
                else: return False
        return (t == ['*'])
        