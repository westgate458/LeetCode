import random
class Solution(object):
	# use hash table to map already-appeared elements to their alternatives
    def __init__(self, n_rows, n_cols):
        """
        :type n_rows: int
        :type n_cols: int
        """
        self.col = n_cols
        self.end = n_rows*n_cols-1
        self.sta = 0
        self.map = {}
            

    def flip(self):
        """
        :rtype: List[int]
        """
        idx = random.randint(self.sta, self.end)
        res = self.map.get(idx, idx)
        self.map[idx] = self.map.get(self.sta, self.sta)        
        self.sta += 1  
        return divmod(res, self.col)

    def reset(self):
        """
        :rtype: None
        """
        self.sta = 0
        self.map = {}


# Your Solution object will be instantiated and called as such:
# obj = Solution(n_rows, n_cols)
# param_1 = obj.flip()
# obj.reset()