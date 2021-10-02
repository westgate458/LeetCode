class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:        
        intervals = sorted(intervals)       
        meetings_end = [intervals[0][1]]        
        for i in intervals[1:]:  
            if meetings_end[0] <= i[0]:
                heapq.heapreplace(meetings_end,i[1])
            else:
                heapq.heappush(meetings_end,i[1])
        return len(meetings_end)