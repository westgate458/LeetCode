class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        d = x = y =0        
        for i in instructions:
            if i == 'L':
                d = (d+3)%4
            elif i == 'R':
                d = (d+1)%4            
            elif i == 'G':
                if d == 0:
                    y += 1
                elif d == 1:
                    x += 1
                elif d == 2:
                    y -= 1
                else:
                    x -= 1
        return d!=0 or (x==0 and y==0)
                
        