# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 21:08:11 2020

@author: Tianqi Guo
"""

class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        # all pointers start from the end
        # p0: first occurance of current character
        # pp: first occurance of next character
        # pt: position to insert new compression, all characters to the right are previous compression
        p0 = pp = pt = lc = len(chars)-1
        # continue compression until the first character is dealt with
        while pp>=0:
            # find all the repetitions of current character
            # after this loop pp should be the next different character
            while pp >= 0 and chars[pp] == chars[p0]: pp -= 1
            # in case of a single character that doesn't need compression
            nn = []
            # check if we have seen repetitions
            if p0 - pp > 1:
                # calculate repetition, convert to string, and break into digits
                nn = list(str(p0-pp))
            # see how many digits the repetition has
            ln = len(nn)
            # we fill the chars array in-place with the character and its repetition number
            chars[pt-ln:pt+1] = [chars[p0]]+nn  
            # pp -> p0: move on to next character        
            # pt-ln-1 -> pt: new insertion point for next compression              
            p0, pt = pp, pt-ln-1
        # total length of compressed string
        l = lc - pt
        # move the compressed string to the front
        chars[:l] = chars[-l:]    
        # return the total length
        return(l)