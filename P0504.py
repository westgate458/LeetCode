class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
		# convert to n-base using divmod
        if num == 0:
            return '0'
        elif num < 0:
            sign = '-'
            num = -num
        else:
            sign = ''
        
        res = []
        while num:
            num, d = divmod(num, 7)
            res.append(d)
        
        return sign+''.join(map(str,(res)))[::-1]  