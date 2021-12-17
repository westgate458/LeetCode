# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """        
        pre = dummy = ListNode(0,head)        
        c = 0
        while c < left-1:
            pre = pre.next
            c += 1    
        t, p = pre.next, None       
        while c < right:
            tt, t.next = t.next, p           
            p, t = t, tt           
            c += 1        
        f, pre.next = pre.next, p     
        if f: f.next = t        
        return dummy.next