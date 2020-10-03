class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
		# group highest frequent tasks into repeated cold-down units
        cnt = Counter(tasks).values()  
        max_cnt = max(cnt) 
        num_max_cnt = cnt.count(max_cnt)       
        return max((n+1)*(max_cnt-1)+num_max_cnt, len(tasks))