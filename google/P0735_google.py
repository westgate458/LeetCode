class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
                res = []        
        for a in asteroids:
            if a > 0: res.append(a)
            else:
                while res and res[-1] > 0 and res[-1]+a<0: res.pop(-1)                  
                if res:
                    if res[-1] > 0 and res[-1]+a==0: res.pop(-1)                   
                    elif (not res) or (res[-1]<0): res.append(a)   
                else: res.append(a) 
        return(res)
                    
                
                