class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        
        N, dp_1, dp_2, dp_3 = len(obstacles)-1, 1, 0, 1       
        
        for o in obstacles:    
            if o == 0:
                dp_1, dp_2, dp_3 = min(dp_1,dp_2+1,dp_3+1), min(dp_1+1,dp_2,dp_3+1), min(dp_1+1,dp_2+1,dp_3)           
            elif o == 1:
                dp_1, dp_2, dp_3 = 1e6, min(dp_2,dp_3+1), min(dp_2+1,dp_3)
            elif o == 2:
                dp_1, dp_2, dp_3 = min(dp_1,dp_3+1), 1e6,  min(dp_1+1,dp_3)
            elif o == 3:
                dp_1, dp_2, dp_3 = min(dp_1,dp_2+1), min(dp_1+1,dp_2), 1e6
            
        return(min(dp_1, dp_2, dp_3))
        
        