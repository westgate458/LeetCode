class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort()
        rooms = [intervals[0][1]]
        for i in intervals[1:]:            
            if i[0] >= rooms[0]:
                heapq.heapreplace(rooms, i[1])
            else:
                heapq.heappush(rooms, i[1])           
        return len(rooms)