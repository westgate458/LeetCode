class Solution {
public:
    void wallsAndGates(vector<vector<int>>& rooms) {
        
        int m = rooms.size(), n = rooms[0].size();        
        vector<int> offset = {0, 1, 0, -1, 0};
        queue<pair<int, int>> q;             
        
        for (int i=0;i<m;i++) {
            for (int j=0;j<n;j++) {                 
                if (rooms[i][j]==0) q.push({i,j}); 
            }            
        }        
        
        while (q.size()>0) {  
            int x = q.front().first, y = q.front().second;
            q.pop();
            for (int k=0;k<4;k++) {
                int xx = x + offset[k], yy = y + offset[k+1];
                if (xx>=0 && xx<m && yy>=0 && yy<n && rooms[xx][yy]>rooms[x][y]+1) {
                    rooms[xx][yy] = rooms[x][y]+1; 
                    q.push({xx,yy});  
                }                                
            } 

        }                    
        
    }
};