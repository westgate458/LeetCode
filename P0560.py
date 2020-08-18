class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
		# hash table for sum occurances
        d, s, res = defaultdict(int), 0, 0        
        for num in nums:
            s += num
            res += d[s-k]
            d[s] += 1        
        return res + d[k]
            
            