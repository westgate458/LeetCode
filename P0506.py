class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
		# simple sorting and keep track of original positions
        l = len(nums)
        t = [p for _,p in sorted(zip(nums,range(l)),reverse=True)]
        places = [-1]*l
        prizes = ["Gold Medal","Silver Medal","Bronze Medal"] + [str(i+1) for i in range(3,l)]
        for i in range(l): 
            places[t[i]] = prizes[i]
        return(places)