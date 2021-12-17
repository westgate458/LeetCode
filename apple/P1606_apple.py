class Solution(object):
    def busiestServers(self, k, arrival, load):
        """
        :type k: int
        :type arrival: List[int]
        :type load: List[int]
        :rtype: List[int]
        """
        jobs = [0]*k
        available = [i for i in range(k)]
        tasks = []        
        for i, (a, l) in enumerate(zip(arrival, load)):            
            while tasks and tasks[0][0] <= a:
                _, server = heapq.heappop(tasks)
                bisect.insort_left(available, server)   
            if available:
                ind = bisect.bisect_left(available, i % k)
                if ind == len(available): ind = 0
                jobs[available[ind]] += 1                
                heapq.heappush(tasks, (a + l, available[ind]))
                del available[ind]         
        m = max(jobs)
        return([i for i in range(k) if jobs[i] == m])