# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 16:23:59 2018

@author: Tianqi Guo
"""
import matplotlib.pyplot as plt; plt.rcdefaults()

import matplotlib.pyplot as plt

height = [5,4,1,2]
l = len(height)


plt.bar(range(l), height, align='center', alpha=0.5)
plt.show()

height_sum = [0]
for i in range(l):
    height_sum.append(height_sum[-1] + height[i])
height_sum.pop(0)

pre = []
h = 0
p = -1
for i in range(l):    
    pre.append([p,h])
    if height[i] >= h:
        h = height[i]
        p = i

pst = []
h = 0
p = l
for i in range(l-1,-1,-1):    
    pst.append([p,h])
    if height[i] >= h:
        h = height[i]
        p = i
        
ans = 0        
i = 0
while i < l - 1:
    print(i)
    
    j = pst[l-1-i][0]    
    while pre[j][0] != i:
        print j
        j = pre[j][0]
        
    
    delta = max(height[i],height[j]) * (j - i - 1) - (height_sum[j-1] - height_sum[i])
    
    ans = ans + delta
    print(i,j,delta,ans)
    i = j   
    
print(ans)
        
    
    
            
    