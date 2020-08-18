class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
		# hash table
        d = defaultdict(int)
        for row in wall:
            s = 0
            for brick in row[:-1]:
                s += brick
                d[s] += 1       
        if not d:
            return len(wall)
        else:
            return(len(wall)-max(d.values()))