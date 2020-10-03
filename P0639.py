class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
		# 0D DP, special states for *
        if s[0] == '0' or '00' in s: return 0  
        l = len(s)          
        if s[0] == '*': 
            ans = [1,9] + [0] * (l-1)
        else:
            ans = [1,1] + [0] * (l-1)     
        for c in range(1,l):     
            if s[c] != '*':
                if s[c] > '0':
                    ans[c+1] = ans[c]  
                if s[c-1] =='1' or (s[c-1] =='2' and s[c] < '7'):
                    ans[c+1] += ans[c-1]
                elif s[c-1] == '*':
                    if s[c] < '7':
                        ans[c+1] += ans[c-1]*2
                    else:
                        ans[c+1] += ans[c-1]                    
            else:     
                if s[c-1] == '1':
                    ans[c+1] += ans[c]*9 + ans[c-1]*9
                elif s[c-1] == '2':
                    ans[c+1] += ans[c]*9 + ans[c-1]*6
                elif s[c-1] == '*':
                    ans[c+1] += ans[c]*9 + ans[c-1]*15
                else:
                    ans[c+1] = ans[c]*9
        return ans[-1]%1000000007