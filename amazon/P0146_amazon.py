class node:
     def __init__(self, key, value):
        self.key = key
        self.val = value
        self.pre = None
        self.nxt = None

class LRUCache:

    def __init__(self, capacity: int):        
        self.key2node = {}
        self.head = node(0,0)
        self.tail = node(0,0)        
        self.head.nxt = self.tail
        self.tail.pre = self.head        
        self.cap = capacity  
        
    def insert(self, key: int, value: int) -> None:                
        n = node(key, value) 
        n.nxt = self.head.nxt
        n.pre = self.head
        n.nxt.pre = n
        self.head.nxt = n            
        self.key2node[key] = n    
        
    def get(self, key: int) -> int:        
        if key not in self.key2node: return -1        
        n = self.key2node[key]
        n.pre.nxt = n.nxt
        n.nxt.pre = n.pre        
        self.insert(key, n.val)        
        return self.key2node[key].val
        

    def put(self, key: int, value: int) -> None:        
        if key in self.key2node:
            n = self.key2node[key]                        
            n.pre.nxt = n.nxt            
            n.nxt.pre = n.pre             
        elif len(self.key2node) == self.cap:           
            n = self.tail.pre
            n.pre.nxt = self.tail
            self.tail.pre = n.pre           
            del self.key2node[n.key]  
        self.insert(key, value)
 

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)