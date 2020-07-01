class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
		# try all divisors and check sum
        if num <= 1: return False
        d = 1
        for i in range(2,int(num**0.5)+1):
            if num%i == 0: d += (i+num/i)
        return (d == num)
        