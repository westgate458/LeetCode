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
        # number of lists and deal with trivial case
        ls = len(lists)
        if ls == 0:
            return None
        
        # set of active pointers
        ps = lists
        
        # initial answer list with arbitrary value
        head = ListNode(-float('inf'))
        p = head
        
        # sorted array formed by one number from each list 
        nums = []      
        # record of which list each number comes from
        inds = []
        
        # take the first number of each list
        # and record which list it comes from
        for i in range(ls):
            if ps[i]:
                nums.append(ps[i].val)
                ps[i] = ps[i].next
                inds.append(i)
        
        # sort the number list from small to large
        # and the index list accordingly        
        yx = zip(nums, inds)
        yx.sort()
        nums = [y for y, x in yx]
        inds = [x for y, x in yx]
        
        # add numbers to answer list until no number is left
        # with insertion of new numbers, the list is maintained sorted along the way
        while nums:
            
            # take the first value in list
            # and its list index
            num = nums.pop(0)
            ind = inds.pop(0)
            
            # add this value to answer list
            p.next = ListNode(num)
            p = p.next            
            
            # if the original list has not reached the end
            # take the remaining first number from that list
            if ps[ind] != None:
                num = ps[ind].val
                ps[ind] = ps[ind].next
            else:                
                continue
            
            # number of remaining numbers in the sorted list
            l_nums = len(nums) 
            
            # if the number list is empty 
            # or the to-be-inserted number is smaller than the first number
            if (l_nums == 0) or (num <= nums[0]):
                # insert the new number as the new first number
                nums.insert(0,num)
                inds.insert(0,ind)   
            else:
                # if the to-be-inserted number is larger than the last number
                if num >= nums[-1]:
                    # insert the new number as the new last number
                    nums.insert(l_nums,num)
                    inds.insert(l_nums,ind)  
                else:
                    # search where to insert the new number
                    left = 0
                    right = l_nums - 1           
                    # each time reduce the search range by half
                    # until the left and right bounds meet
                    while right - left > 1:
                        # compare the new number with the median of the current range
                        mid = (left + right)/2
                        # update the search range accordingly
                        if nums[mid] <= num:
                            left = mid
                        else:
                            right = mid
                    # insert the new number to the sorted list
                    # at desired positioin
                    if nums[left] < num:
                        nums.insert(left+1,num)
                        inds.insert(left+1,ind)
                    else:
                        nums.insert(left,num)
                        inds.insert(left,ind)        
        
        # return the combined sorted list of nodes
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