class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        c = defaultdict(int)
        pos = []
        neg = []
        for n in nums:
            if n >= 0: pos.append(n)
            elif n < 0: neg.append(n)
            c[n] += 1
        res = set()
        if (0 in c) and (c[0]>=3):
            res.add((0,0,0))        
        for i in pos:
            for j in neg:
                k = -i-j
                if k in c:
                    if (k==i or k==j) and (c[k]==1): continue
                    if k < j: res.add((k,j,i))
                    elif k > i: res.add((j,i,k))
                    else: res.add((j,k,i))                        
        return list(res)