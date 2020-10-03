class Solution(object):
    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
		# one pointer for each list, use heap to access smallest among all
        ls, hp = [len(num) for num in nums], []        
        for i, n in enumerate(nums):
            heapq.heappush(hp, (n[0], i, 0))            
        mx = max([n[0] for n in hp])
        res = (hp[0][0], mx)
        min_range = res[1] - res[0]        
        while hp:
            mn, i, j = heapq.heappop(hp)
            cur_range = mx - mn
            if cur_range < min_range:
                min_range = cur_range
                res = (mn, mx)
            j += 1
            if j < ls[i]:
                heapq.heappush(hp, (nums[i][j], i, j))
                mx = max(mx, nums[i][j])                
            else:
                break
        return res