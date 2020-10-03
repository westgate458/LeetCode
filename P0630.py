class Solution(object):
    def scheduleCourse(self, courses):
        """
        :type courses: List[List[int]]
        :rtype: int
        """  
		# sort by ddl, then use heap to replace course with longest duration
        ts, t_end = [], 0        
        for t, d in sorted(courses,key=lambda x: x[1]):            
            if t + t_end <= d:
                t_end += t
                heappush(ts, -t)
            elif ts and t <= -ts[0]:                    
                t_end = t_end + heapq.heappop(ts) + t 
                heappush(ts, -t)        
        return(len(ts))
            