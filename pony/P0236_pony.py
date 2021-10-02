# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def DFS(node):
            if node == None:                
                return ('#', False, False)    
            
            res_l, foundP_l, foundQ_l = DFS(node.left)
            if res_l != '#':
                return (res_l, True, True)
            if (foundP_l and node == q) or (foundQ_l and node == p):
                return (node, True, True)          
            
            res_r, foundP_r, foundQ_r = DFS(node.right) 
            if res_r != '#':
                return (res_r, True, True)
            if (foundP_r and node == q) or (foundQ_r and node == p) or (foundP_r and foundQ_l) or (foundP_l and foundQ_r):
                return (node, True, True)      
            
            return ('#', foundP_l or foundP_r or (node == p), foundQ_l or foundQ_r or (node == q))  

        return DFS(root)[0]
                
            