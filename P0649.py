class Solution(object):
    def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        """
		# similar to pairing parentheses, greedy by prioritizing cancels after then before
        while ('R' in senate) and ('D' in senate):                       
            s, v = '', 0                        
            for c in senate:
                if c == 'D':
                    if v >= 0: s += 'D'
                    v += 1
                else:
                    if v <= 0: s += 'R'                    
                    v -= 1            
            i = 0
            while v < 0 and i < len(s):
                if s[i] == 'D':
                    s = s[:i] + s[i+1:]
                    v += 1
                else:
                    i += 1
            while v > 0 and i < len(s):
                if s[i] == 'R':
                    s = s[:i] + s[i+1:]
                    v -= 1
                else:
                    i += 1            
            senate = s  
        return 'Radiant' if senate[0]=='R' else 'Dire'
     
                        