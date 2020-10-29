# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """
		# fill in elements to 2D matrix using queue
        def helper(node):
            if not node: return 0
            return max(helper(node.left),helper(node.right))+1        
        d = helper(root)        
        w = 2**d-1        
        res = [[""] * w for _ in range(d)]
        s = [(root, 0, w//2, (w+1)//4)]
        while s:
            node, lvl, pos, sft = s.pop()
            res[lvl][pos] = str(node.val)
            if node.left: s.append((node.left, lvl+1, pos-sft, sft//2))
            if node.right: s.append((node.right, lvl+1, pos+sft, sft//2))        
        return res