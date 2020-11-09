class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
		# dictionary for ending numbers at each LIS position 
        if not nums: return 0
        nums_sorted = [float('-inf')]
        max_lengths = [{float('-inf'):1}]        
        for num in nums + [float('inf')]:        
            i = bisect.bisect_left(nums_sorted, num)            
            if i == len(nums_sorted):
                nums_sorted.append(num)
                max_lengths.append(defaultdict(int))
            else:
                nums_sorted[i] = num   
            for n in max_lengths[i-1]:
                if n < num:
                    max_lengths[i][num] += max_lengths[i-1][n] 
        return max_lengths[-1].values()[0]
