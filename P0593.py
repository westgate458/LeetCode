class Solution(object):
    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """        
		# check distances between corners
        def l(p1, p2): return (p1[1] - p2[1])**2 + (p1[0] - p2[0])**2         
        return len(set([tuple(p1),tuple(p2),tuple(p3),tuple(p4)]))==4 and \
               len(set([l(p1, p2),l(p1, p3),l(p1, p4),l(p2, p3),l(p2, p4),l(p3, p4)]))==2