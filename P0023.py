# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 21:01:46 2018

@author: Tianqi Guo
"""

# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None
         
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        ls = len(lists)
        if ls == 0:
            return None
        
        num_inf = float('inf')        
        ps = lists
        head = ListNode(-num_inf)
        p = head
        
        nums = []      
        inds = []
        for i in range(ls):
            if ps[i]:
                nums.append(ps[i].val)
                ps[i] = ps[i].next
                inds.append(i)
        yx = zip(nums, inds)
        yx.sort()
        nums = [y for y, x in yx]
        inds = [x for y, x in yx]
        
        while nums:
            
            num = nums.pop(0)
            ind = inds.pop(0)
            
            p.next = ListNode(num)
            p = p.next            
            
            if ps[ind] != None:
                num = ps[ind].val
                ps[ind] = ps[ind].next
            else:
                continue
            
            l_nums = len(nums) 
            
            if (l_nums == 0) or (num <= nums[0]):
                nums.insert(0,num)
                inds.insert(0,ind)   
            else:
                if num >= nums[-1]:
                    nums.insert(l_nums,num)
                    inds.insert(l_nums,ind)  
                else:
                    left = 0
                    right = l_nums - 1           
                    while right - left > 1:
                        mid = (left + right)/2
                        if nums[mid] <= num:
                            left = mid
                        else:
                            right = mid
                    if nums[left] < num:
                        nums.insert(left+1,num)
                        inds.insert(left+1,ind)
                    else:
                        nums.insert(left,num)
                        inds.insert(left,ind)        
                
        return head.next          
         
 
nums_list = [[-9,-7,-7],[-6,-4,-1,1],[-6,-5,-2,0,0,1,2],[-9,-8,-6,-5,-4,1,2,4],[-10],[-5,2,3]]
lists = []

for i in range(len(nums_list)):    
    nums = nums_list[i]
    l = ListNode(nums[0])
    p = l
    for i in range(1,len(nums)):
        p.next = ListNode(nums[i])
        p = p.next    
    lists.append(l)
    
test = Solution()
p = test.mergeKLists(lists)
      
while p != None:
    print(p.val)      
    p = p.next