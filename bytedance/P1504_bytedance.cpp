class Solution {
public:
    int numSubmat(vector<vector<int>>& mat) {        
        int m = mat.size(), n = mat[0].size();
        vector<vector<int>> num(m,vector<int>(n,0));
        int res = 0;
        for (int i=0;i<m;i++) {
            for (int j=0;j<n;j++) {                
                if (mat[i][j]!=0) {
                    if (j==0) num[i][j] = 1;
                    else num[i][j] = num[i][j-1]+1;
                    res += num[i][j];
                    int ones = num[i][j];
                    for (int k = i-1;k>=0;k--) {
                        ones = min(ones, num[k][j]);
                        res += ones;
                    }   
                }  
            }  
        }  
        return(res);        
    }
};