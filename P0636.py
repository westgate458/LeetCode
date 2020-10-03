class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
		# simple stack
        s, d = [(n,0)], [0] * (n+1)           
        for log in logs:
            temp = log.split(':')   
            if temp[1] == 'start':
                s.append((int(temp[0]), temp[2]))
            else:
                _, t = s.pop()
                duration = int(temp[2]) - int(t) + 1
                d[int(temp[0])] += duration
                d[s[-1][0]] -= duration        
        return(d[:n])