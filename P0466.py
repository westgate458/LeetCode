# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 21:06:10 2020

@author: Tianqi Guo
"""

class Solution(object):
    def getMaxRepetitions(self, s1, n1, s2, n2):
        """
        :type s1: str
        :type n1: int
        :type s2: str
        :type n2: int
        :rtype: int
        """
        # check trivial case: s2 has characters not present in s1
        if not set(s2).issubset(set(s1)):
            return 0
        
        # p1, p2: pointers to traverse two strings
        # l1, l2: lengths of two strings
        p1, p2, l1, l2 = 0, 0, len(s1), len(s2)             
        # index_to_look: at the start of each repetition of s1, 
        #                which position in s2 has the character to macth in s1,
        #                when a position appears the 2nd time in this list
        #                between last apperance and previous index is the repeating pattern
        # repeats: for each index in the above list, which repetition of s2 it was associated with
        index_to_look, repeats = [], []  
        # repetition of each string before the pattern is found
        repeat_1, repeat_2 = 1, 1
        
        # look for the repeating pattern
        # each loop is a repetition of s1
        while True:            
            # at the start of this s1, record the repetition of s2 so far
            repeats.append(repeat_2)
            # if in one of previous s1, we have seen this p2
            # it means a pattern has been found
            if p2 in index_to_look: break
            # otherwise record this p2 for later check
            else: index_to_look.append(p2)   
            # for each character in s1                
            for p1 in xrange(l1):
                # if it is a match for current character in s2
                # move on to next character in s2
                if s1[p1] == s2[p2]: p2 += 1
                # if we have reached the end of s2
                # start a new one and update its repetition
                if p2 == l2: p2, repeat_2 = 0, repeat_2+1
            # at the end of s1, return to the start and update its repetition        
            repeat_1 += 1                    
        
        # after the pattern has been found, we segment S1=s1*n1 into three partitions:
        # HEAD||REPEATING BLOCKS||TAIL
        
        # last time we saw p2 is where the repeating block started,
        # its index in index_to_look is the number of repetition of s1 when HEAD ends
        block_start = index_to_look.index(p2)
        # how many s1 in the repeating block, current repetition of s1 is repeat_1
        block_length = repeat_1 - block_start - 1
        # how many repeating blocks in S1=s1*n1
        block_repeats = (n1 - block_start)//block_length
        # after the repeating blocks, how many s1 left afterwards in TAIL
        block_at_end = (n1 - block_start)%block_length

        # for the three partitions, we then figure out how many s2 each one correspond to
        # those have been solve in the loop above and recorded in repeats
        
        # in HEAD, how many s2 can we find          
        s2_bfr_block = repeats[block_start] - 1        
        # in REPEATING BLOCKS, how many s2 in each block
        s2_per_block = repeats[-1] - repeats[block_start]  
        # in TAIL, how many s2 can we find
        # TAIL is unfinished repeating block, and the number of s2 it contains
        # can be obtained by looking at first 'block_at_end'*s1 in the repeating block
        # which is recorded in repeats from [block_start] to [block_start+block_at_end]
        s2_aft_block = repeats[block_start+block_at_end] - repeats[block_start]
        
        # sum up all s2 repetitions, then the repetition of S2 is 1//n2
        return (s2_bfr_block + s2_per_block*block_repeats + s2_aft_block)//n2
        