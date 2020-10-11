class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
		# sorting by interval ends and greedy, same as P0435
        c, e = 0, float('-inf')
        for a, b in sorted(pairs, key=lambda x: x[1]):
            if a > e: c, e = c+1, b
        return c