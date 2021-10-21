class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {        
        int m = grid.size();
        int n = grid[0].size();
        int res = 0;
        vector<int> dij{-1,0,1};        
        vector<vector<int>> s;
        for (int i=0;i<m;i++) {
            for (int j=0;j<n;j++) {
                if (grid[i][j] == '1') {
                    vector<int> ij{i,j};
                    s.push_back(ij);
                    grid[i][j] = '0';
                    res ++;                    
                    while (s.size()>0) {                        
                        vector<int> ij = s.back();
                        s.pop_back();
                        int ii = ij[0];
                        int jj = ij[1];
                        for (int di:dij) {
                            for (int dj:dij)  {
                                if (di*dj!=0) continue;
                                int a = ii + di;
                                int b = jj + dj;
                                if ((a>=0) and (a<m) and (b>=0) and (b<n) and (grid[a][b]=='1')) {
                                    grid[a][b] = '0';
                                    vector<int> ij{a,b};
                                    s.push_back(ij);
                                }
                                
                            }
                        }
                    }
                }
            }
        }
        return(res);
    }
};