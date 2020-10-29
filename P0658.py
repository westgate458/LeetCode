class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
		# search for the start of the subsequence
        i, j = 0, len(arr)-k        
        while i < j:
            m = (i+j)//2
            if x - arr[m] > arr[m+k] - x:
                i = m + 1
            else:
                j = m
        return arr[i:i+k]