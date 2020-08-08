class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """        
		# reverse by groups
        res = '' 
        for nn in range(len(s)//k+1):                 
            if nn%2 == 0: res += s[nn*k:(nn+1)*k][::-1]
            else: res += s[nn*k:(nn+1)*k]           
        return(res)         