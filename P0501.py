# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import defaultdict
class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """               
		
		# for BST, in-order traversal gives the sorted list of all nodes
		# find the mode in the sorted list is trivial
		
        pre, count, max_count = float('inf'), 1, -1
        p, s, res = root, [], []      
        
        while p or s:
            if p:                  
                s.append(p)                           
                p = p.left
            else:              
				# when a None node is encountered, we need to go back to previous node
				# for the previous node, accessing its value is 'in-order' traversal since
				# all of its left subtree has been accessed already
				# now check if it has appeared more the the mode
                if s[-1].val == pre:
                    count += 1
                else:
                    count = 1
                if count == max_count:
                    res.append(s[-1].val)
                elif count > max_count:
                    max_count = count
                    res = [s[-1].val]
                pre = s[-1].val                
                p = s[-1].right  
                s.pop()              
        return res