# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 20:23:37 2019

@author: Tianqi Guo
"""

from collections import defaultdict
class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        
        # Solution 1 beats 99.56%: greedy DFS
        # d[from] = [to's]
        d = defaultdict(list)     
        # sort tickets from large to small
        # so in each d[from], smallest to is at the end to pop
        for de, ar in sorted(tickets, reverse=True):
            # add current ticket to dictionary
            d[de].append(ar)
        # constructed itinerary
        self.iternerary = []
        # subfunction for construct the itinerary
        def DFS(de):
            # for current airport, for all its destinations remained at current level
            while d[de]:
                # pop the destination at the end (smallest)
                # continue DFS from the new airport
                DFS(d[de].pop())
            # we start from the smallest (greedy), so the smallest will be DFS'ed first
            # and when it is added to the itinerary here in next level of DFS
            # all other destinations of current airport have been added to itinerary
            # already in deeper DFS levels due to loops back to current airport
            self.iternerary.append(de)
        # start DFS from JFK
        DFS('JFK')
        # first added airports in deeper DFS levels are larger
        # so in reversed order we get the smallest lexical order
        return self.iternerary[::-1]
        
#        # Solution 2 beats 20.27%: regular DFS
#        d = defaultdict(list)       
#        self.res = []
#        for de, ar in tickets:
#            d[de] += [ar]           
# 
#        for key in d:
#            d[key].sort()  
#        
#        def DFS(de, itinerary, stop):
#            if not stop:
#                return itinerary
#            elif d[de]:
#                pre = None
#                for idx, ar in enumerate(d[de]):
#                    if ar == pre:
#                        continue
#                    d[de] = d[de][:idx] + d[de][idx+1:]
#                    t = DFS(ar, itinerary + [ar], stop - 1) 
#                    if t:
#                        return t
#                    d[de] = d[de][:idx] + [ar] + d[de][idx:]
#                    pre = ar
#            else:
#                return None               
#        return DFS('JFK',['JFK'], len(tickets))

tickets = [["AXA","EZE"],["EZE","AUA"],["ADL","JFK"],["ADL","TIA"],["AUA","AXA"],["EZE","TIA"],["EZE","TIA"],["AXA","EZE"],["EZE","ADL"],["ANU","EZE"],["TIA","EZE"],["JFK","ADL"],["AUA","JFK"],["JFK","EZE"],["EZE","ANU"],["ADL","AUA"],["ANU","AXA"],["AXA","ADL"],["AUA","JFK"],["EZE","ADL"],["ANU","TIA"],["AUA","JFK"],["TIA","JFK"],["EZE","AUA"],["AXA","EZE"],["AUA","ANU"],["ADL","AXA"],["EZE","ADL"],["AUA","ANU"],["AXA","EZE"],["TIA","AUA"],["AXA","EZE"],["AUA","SYD"],["ADL","JFK"],["EZE","AUA"],["ADL","ANU"],["AUA","TIA"],["ADL","EZE"],["TIA","JFK"],["AXA","ANU"],["JFK","AXA"],["JFK","ADL"],["ADL","EZE"],["AXA","TIA"],["JFK","AUA"],["ADL","EZE"],["JFK","ADL"],["ADL","AXA"],["TIA","AUA"],["AXA","JFK"],["ADL","AUA"],["TIA","JFK"],["JFK","ADL"],["JFK","ADL"],["ANU","AXA"],["TIA","AXA"],["EZE","JFK"],["EZE","AXA"],["ADL","TIA"],["JFK","AUA"],["TIA","EZE"],["EZE","ADL"],["JFK","ANU"],["TIA","AUA"],["EZE","ADL"],["ADL","JFK"],["ANU","AXA"],["AUA","AXA"],["ANU","EZE"],["ADL","AXA"],["ANU","AXA"],["TIA","ADL"],["JFK","ADL"],["JFK","TIA"],["AUA","ADL"],["AUA","TIA"],["TIA","JFK"],["EZE","JFK"],["AUA","ADL"],["ADL","AUA"],["EZE","ANU"],["ADL","ANU"],["AUA","AXA"],["AXA","TIA"],["AXA","TIA"],["ADL","AXA"],["EZE","AXA"],["AXA","JFK"],["JFK","AUA"],["ANU","ADL"],["AXA","TIA"],["ANU","AUA"],["JFK","EZE"],["AXA","ADL"],["TIA","EZE"],["JFK","AXA"],["AXA","ADL"],["EZE","AUA"],["AXA","ANU"],["ADL","EZE"],["AUA","EZE"]]
test = Solution()
print(test.findItinerary(tickets))