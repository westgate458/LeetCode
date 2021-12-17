# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeZeroSumSublists(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # Solution 1: converting to list
        nums = []
        while head:
            s = 0
            for i in range(len(nums)-1,-1,-1):
                s += nums[i]
                if s + head.val == 0:
                    nums = nums[:i]
                    s = None
                    break
            if s != None and head.val !=0:
                nums.append(head.val)
            head = head.next               
        
        dummy = ListNode()
        p = dummy
        for n in nums:
            p.next = ListNode(n)
            p = p.next
        return dummy.next
        
        # Solution 2: using dictionary
        p = dummy = ListNode(0,head)
        d = {}
        s = 0      
        while p:
            s += p.val
            d[s] = p
            p = p.next
        
        p = dummy
        s = 0
        while p:
            s += p.val
            p.next = d[s].next
            p = p.next
        
        return dummy.next
        
        