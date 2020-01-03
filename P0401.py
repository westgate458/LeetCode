# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 21:52:51 2020

@author: Tianqi Guo
"""

class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """        
        # Solution 1 beats 97.19% : one-liner
        return(['%d:%0.2d'%(h,m) for h in xrange(12) for m in xrange(60) if (bin(h)+ bin(m)).count('1') == num])
        # Solution 2 beats 88.52%: generator and yield
        def getPos(pos, num, i):
            if num == 0:
                yield pos
            else:
                for j in xrange(i,11-num):
                    for k in getPos(pos+[j],num-1,j+1):
                        yield k
        res = []
        for pos in getPos([],num,0):            
            s = ''.join(['1' if i in pos else '0' for i in xrange(10)])
            h, m = int(s[:4],2), int(s[4:],2)            
            if h < 12 and m < 60:
                res.append('%d:%0.2d'%(h,m))
        return(res)