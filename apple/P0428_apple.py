"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """
        if not root: return None
        res = []
        l = [root,'*']
        while l:            
            ll = []
            for n in l:
                if n=='*':
                    res.append('*')
                else:
                    res.append(str(n.val))
                    for nn in n.children:
                        ll.append(nn)
                    ll.append('*')
            l = ll 
        return ','.join(res)        
    
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """
        if not data: return None
        data = data.split(',')      
        root = Node(0,[])
        l1 = [root]
        l2 = []
        i = 0
        for n in data:
            if n == '*':
                i += 1
                if i == len(l1):
                    l1 = l2
                    l2 = []
                    i = 0
            else:
                nn = Node(int(n),[])                
                l1[i].children.append(nn)
                l2.append(nn)
        return root.children[0]        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))