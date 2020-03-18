# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 22:07:10 2020

@author: Tianqi Guo
"""

class Solution(object):
    def validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str
        """
        # check IPv4 case
        if '.' in IP:
            # split into groups
            nums = IP.split('.')
            # IPv4 has 4 groups
            if len(nums) != 4:
                return 'Neither'                
            # check each group
            for num in nums:
                # group needs to be non-empty and has not prefix 0
                if not num or (num != '0' and num[0] == '0'):
                    return 'Neither'                    
                # group needs to be digits only
                for d in num:
                    if d not in "0123456789":
                        return "Neither"
                # group needs to be no larger than 255
                if int(num)>255:
                    return 'Neither'                
            # it is valid to this point
            return 'IPv4'
        # check IPv6 case
        elif ':' in IP:
            # split into groups
            nums = IP.split(':')
            # IPv6 has 8 groups
            if len(nums) != 8:
                return 'Neither' 
            # check each group
            for num in nums:
                # group needs to be non-empty and no longer than 4
                if not num or len(num) > 4:
                    return 'Neither'
                # group needs to be a hex number
                for d in num:
                    if d not in "0123456789abcdefABCDEF":
                        return 'Neither'                        
            # it is valid to this point
            return 'IPv6'
        else:
            # not valid
            return 'Neither'