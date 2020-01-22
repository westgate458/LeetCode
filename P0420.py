# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 22:26:18 2020

@author: Tianqi Guo
"""

class Solution(object):
    def strongPasswordChecker(self, s):
        """
        :type s: str
        :rtype: int
        """
        # length of the password
        l = len(s)        
        # flag if the password has all three required types
        has_upper = has_lower = has_digit = 0            
        # repeats: of each character in a row
        # pre: previous character
        repeats, repeat, pre = [], 0, ''     
        # check each character
        for c in s+'.':
            # if current character is a repetition of the previous character
            if c == pre:
                # update the count
                repeat += 1
            # if current character is a new one
            else:
                # only record the repeat if it is 3 or more
                # since we do not need to change repeats of 1 or 2 
                if repeat > 2:
                    repeats.append(repeat)
                # udpate pre and reset counter
                pre, repeat = c, 1                   
            # check if all three types occur
            has_upper = has_upper or c.isupper()            
            has_lower = has_lower or c.islower()
            has_digit = has_digit or c.isdigit()                             
        # total number of types that appeared
        has_types = has_upper + has_lower + has_digit
        # for all character repeats >= 3
        # we take mod of the repeat, and construct a new list
        heap = [(repeat%3,repeat) for repeat in repeats]     
        # number of characters we need to delete
        delete_count = 0        
        # if length of password is shorter than 6
        if l < 6:               
            # deal with a trivial case where a single character appeared 5 times in a row (e.g. 'aaaaa')
            if repeats and repeats[-1] == 5:
                # minimum operation is change one character -> 'aaAaa'
                # then add one character -> 'aaAaa0'
                return 2
            # if more complicated case
            else:
                # we need to do
                # 1) add (6-l) characters to make the minimum length
                # 2) change or add (3-has_types) characters to make all three types appear
                # operations needed are the larger from the two
                return max(6-l, 3-has_types)
        # if length of password is longer than 20
        elif l > 20:           
            # we need to delete (l-20) characters no matter what
            delete_count = l-20
            # make the constructed list a heap
            heapq.heapify(heap)   
            # continue deleting characters until length is 20
            while heap and l > 20:
                # take the smallest mod
                # since we prefer to delete 1 a from 'aaa'(mod=0) 
                # than 2 a's from 'aaaa' (mod=1) 
                # or   3 a's from 'aaaaa'(mod=2)
                # since for 'aaaa' and 'aaaaa' it requires more deleting operations
                # and if we save them for later we can change a character to satisfy type requirement
                # and deal with repetition as well
                m, r = heapq.heappop(heap)
                # the number of deletion operations to get to 'aa'
                # but we dont need to delete more than needed to get to 20
                l_change = min(m+1, l-20)
                # update the length of the password
                l -= l_change                
                # push new repeat of characters to heap
                heapq.heappush(heap, (2, r-l_change))   
        # after deletion, the final operations still needed are 
        # 1) the changes to satisfy type requirements
        # 2) the changes to break three-peats
        # the 1) can be achieved by 2) if possible
        change_count = max(sum([r//3 for _, r in heap]), 3-has_types)        
        # return the total number of operations needed
        return change_count + delete_count
                
            