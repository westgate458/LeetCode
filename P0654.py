# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
		# Solution 1 beats 99.71%: monotonically decreasing stack
        s = [TreeNode(nums[0])]
        for n in nums[1:]:
            node = TreeNode(n)
            if n < s[-1].val:
                s[-1].right = node
            else:
                while s and n > s[-1].val:                    
                    node.left = s.pop()
                if s:
                    s[-1].right = node
            s.append(node)
        return s[0]
            
        # Solution 2 beats 77.23%: naive recursion
       def construct(i, j):
            if i == j:
                return TreeNode(nums[i])
            elif i > j:
                return None
            m = -1            
            kk = -1
            for k in range(i, j+1):
                if nums[k] > m:
                    m = nums[k]
                    kk = k
            return TreeNode(m, construct(i,kk-1),construct(kk+1,j))
        
        return construct(0,len(nums)-1)		