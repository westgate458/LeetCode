class Solution {
public:
	// look at each cell individually
    vector<vector<int>> imageSmoother(vector<vector<int>>& M) {
        int m = M.size(), n = M[0].size();        
        vector<vector<int>> R(m, vector<int>(n,0));
        for (int i=0;i<m;i++) {
            for (int j=0;j<n;j++) {
                int s = 0, c = 0;                
                if (i>0) {
                    if (j>0) {
                        s += M[i-1][j-1];
                        c += 1;
                    }
                    s += M[i-1][j];
                    c += 1;
                    if (j<n-1) {
                        s += M[i-1][j+1];
                        c += 1;
                    }
                }
                if (j>0) {
                    s += M[i][j-1];
                    c += 1;
                }
                s += M[i][j];
                c += 1;
                if (j<n-1) {
                    s += M[i][j+1];
                    c += 1;
                }
                if (i<m-1) {
                    if (j>0) {
                        s += M[i+1][j-1];
                        c += 1;
                    }
                    s += M[i+1][j];
                    c += 1;
                    if (j<n-1) {
                        s += M[i+1][j+1];
                        c += 1;
                    }
                }            
            R[i][j] = floor(s/c);
            }
        }
        return R;        
    }
};