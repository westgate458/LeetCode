class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """     
		# sort and keep track of original positions then find discrepency
        s = str(num)
        l = len(s)
        ss = sorted(zip(s,range(l)),reverse=True)                
        for i in range(l):
            if s[i] != ss[i][0]:
                k = i
                while (k > 0) and (ss[k-1][0] == ss[k][0]): k -= 1                
                return(s[:i]+ss[i][0]+s[i+1:ss[k][1]]+s[i]+s[ss[k][1]+1:])
        return num