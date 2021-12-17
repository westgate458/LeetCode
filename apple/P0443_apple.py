class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """        
        pre, i, k = chars[0], 0, 1
        for c in chars[1:]+['*']:
            if c == pre: k += 1
            else:
                chars[i] = pre
                if k > 1:
                    kk = str(k)                    
                    chars[i+1:i+len(kk)] = kk                    
                    i += len(kk)                    
                i += 1
                k, pre = 1, c                          
        return i