# The read4 API is already defined for you.
# def read4(buf4: List[str]) -> int:

class Solution:
    def __init__(self):
        self.temp = []
        
    def read(self, buf: List[str], n: int) -> int:        
        buf4 = ['']*4                
        m = read4(buf4)        
        while m > 0:
            self.temp = self.temp + buf4[:m]
            buf4 = ['']*4
            m = read4(buf4)        
        self.temp = self.temp + buf4[:m]        
        buf[:n] = self.temp[:n]
        l = len(self.temp[:n])
        self.temp = self.temp[n:] 
        return l

        