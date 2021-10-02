class SparseVector:
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.d = {i:v for i,v in enumerate(nums) if v}

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec):
        """
        :type vec: 'SparseVector'
        :rtype: int
        """
        return sum([self.d[i] * vec.d[i] for i in vec.d if i in self.d])

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)