class Solution(object):
    def visiblePoints(self, points, angle, location):
        """
        :type points: List[List[int]]
        :type angle: int
        :type location: List[int]
        :rtype: int
        """        
        angles = []
        origin = 0
        for x, y in points:            
            if x == location[0]:
                if y > location[1]: angles.append(90)
                elif y < location[1]: angles.append(-90)
                else: origin += 1
            elif x > location[0]: angles.append(math.atan(float(y - location[1])/(x - location[0]))/math.pi*180)
            else: angles.append(math.atan(float(y - location[1])/(x - location[0]))/math.pi*180+180)
        
        angles.sort()
        angles = angles + [a+360 for a in angles]        
        i = 0
        for j in range(len(angles)):
            if angles[j] - angles[i] > angle: i += 1            
        return len(angles)-i+origin