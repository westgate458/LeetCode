class Solution {
public:
    int shortestDistance(vector<vector<int>>& grid) {        
        int m = grid.size(), n = grid[0].size();        
        vector<vector<int>> res(m, vector<int>(n,0));
        vector<vector<int>> buildings(m, vector<int>(n,0));        
        queue <pair<int,int>> q;
        vector<int> shift{0,1,0,-1,0};
        int n_buildings = 0;        
        for (int i=0;i<m;i++) {            
            for (int j=0;j<n;j++) {                
                if (grid[i][j]==2) res[i][j] = INT_MAX;                
                if (grid[i][j]==1) {
                    n_buildings ++;
                    vector<vector<int>> dis(m, vector<int>(n,INT_MAX));
                    res[i][j] = INT_MAX;                    
                    dis[i][j] = 0;
                    q.push(pair{i,j});                    
                    while (q.size()>0) {                        
                        auto p = q.front();
                        q.pop();
                        int x = p.first;
                        int y = p.second;                        
                        for (int k=0;k<4;k++) {
                            int xx = x + shift[k];
                            int yy = y + shift[k+1];                            
                            if (xx>=0 && xx<m && yy>=0 && yy<n && grid[xx][yy]==0 && dis[xx][yy]>dis[x][y]+1) {
                                dis[xx][yy] = dis[x][y]+1;
                                res[xx][yy] += dis[xx][yy];
                                buildings[xx][yy] ++;
                                q.push(pair{xx,yy});
                            }
                        }                        
                    }  
                }            
            }            
        }        
        int min_dis = INT_MAX;
        for (int i=0;i<m;i++) {            
            for (int j=0;j<n;j++) {
                if (res[i][j]>0 && buildings[i][j]==n_buildings) min_dis = min(min_dis, res[i][j]);
            }         
        }        
        if (min_dis == INT_MAX) return -1;
        return(min_dis);
    }
};