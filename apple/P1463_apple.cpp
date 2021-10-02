class Solution {
public:
    int cherryPickup(vector<vector<int>>& grid) {
        
        int n = grid[0].size();
        
        vector<vector<int>> dp_0(n, vector<int>(n,0));        
        dp_0[0][n-1] = grid[0][0]+grid[0][n-1];        
        
        int res = 0;
        for (int i = 1; i < grid.size(); i++) {
            vector<vector<int>> dp_1(n, vector<int>(n,0));
            for (int j=0; j<=min(i,n-1); j++) {
                for (int k=max(j,n-i-1); k<n; k++) { 
                    for (int jj=max(j-1,0);jj<=min(j+1,n-1);jj++) {
                        for (int kk=max(k-1,0);kk<=min(k+1,n-1);kk++) {
                            dp_1[j][k] = max(dp_1[j][k], dp_0[jj][kk]);
                        }                       
                    } 
                    if (j!=k) dp_1[j][k] += grid[i][j] + grid[i][k];
                    else dp_1[j][k] += grid[i][j];                    
                }
            }
            dp_0 = dp_1;
        } 
        for (int j=0; j<n; j++) {
            for (int k=0; k<n; k++) {  
                res = max(res, dp_0[j][k]);
            }
        }        
        return(res);
    }
};