class Solution(object):
	# mapping each number onto a real line with segment length equal to weight
    def __init__(self, w):
        """
        :type w: List[int]
        """        
        self.nums = [0]*(len(w)+1)
        for i, ww in enumerate(w): self.nums[i+1] = self.nums[i] + ww
    def pickIndex(self):
        """
        :rtype: int
        """
        return bisect.bisect_left(self.nums, random.randint(1,self.nums[-1]))-1        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()