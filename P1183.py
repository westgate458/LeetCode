# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 21:42:37 2020

@author: Tianqi Guo
"""

class Solution(object):
    def maximumNumberOfOnes(self, width, height, sideLength, maxOnes):
        """
        :type width: int
        :type height: int
        :type sideLength: int
        :type maxOnes: int
        :rtype: int
        """        
        n_win_w, n_win_h = width//sideLength, height//sideLength  
        ll_w, ll_h = width - n_win_w*sideLength, height - n_win_h*sideLength
        ones_total = n_win_w*n_win_h*maxOnes + (n_win_w+n_win_h+1)*min(maxOnes,ll_w*ll_h)        
        remain_ones = maxOnes - ll_w*ll_h        
        if remain_ones > 0:
            n_x_max, n_y_max = min(remain_ones,(sideLength - ll_w)*ll_h), min(remain_ones,(sideLength - ll_h)*ll_w)
            if n_x_max + n_y_max <= remain_ones:
                ones_total += (n_x_max*n_win_w + n_y_max*n_win_h)
            elif n_win_w >= n_win_h:
                ones_total += n_x_max*n_win_w + (remain_ones-n_x_max)*n_win_h
            else:
                ones_total += (remain_ones-n_y_max)*n_win_w + n_y_max*n_win_h   
        return ones_total