class Solution(object):
    def findLUSlength(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
		# longer string is the Longest Uncommon Subsequence
        return -1 if a == b else max(len(a), len(b))  