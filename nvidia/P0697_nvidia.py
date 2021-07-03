class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        pos = defaultdict(list)
        degree = 0
        for i, num in enumerate(nums):
            pos[num] += [i]
            if len(pos[num])>degree:
                degree = len(pos[num])
                res = pos[num][-1]-pos[num][0]+1      
            elif len(pos[num])==degree:
                if pos[num][-1]-pos[num][0]+1 < res:
                    res = pos[num][-1]-pos[num][0]+1        
        return(res)
        
        