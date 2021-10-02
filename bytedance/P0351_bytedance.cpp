class Solution {
    
private:
        
    unordered_map<int,int> status;
    
    bool check_cross(int visited, int n) {
        return(((visited>>n) &1) != 1);        
    }    
    int DFS(int s, int last, int visited) {        
        int code = visited + (last<<10);
        if (status.find(code) != status.end()) {
            return(status[code]);
        }        
        if (s==0) return 1;
        int res = 0;
        for (int i=1;i<=9;i++) {            
            if (((visited>>i)&1) != 1) {
                if (last == 1) {
                    if (i==3 && check_cross(visited, 2)) continue;
                    if (i==7 && check_cross(visited, 4)) continue;    
                    if (i==9 && check_cross(visited, 5)) continue;
                }
                else if (last == 2) {
                    if (i==8 && check_cross(visited, 5)) continue;
                }
                else if (last == 3) {
                    if (i==1 && check_cross(visited, 2)) continue;
                    if (i==7 && check_cross(visited, 5)) continue;    
                    if (i==9 && check_cross(visited, 6)) continue;
                }
                else if (last == 4) {
                    if (i==6 && check_cross(visited, 5)) continue;
                }
                else if (last == 6) {
                    if (i==4 && check_cross(visited, 5)) continue;
                }
                else if (last == 7) {
                    if (i==1 && check_cross(visited, 4)) continue;
                    if (i==3 && check_cross(visited, 5)) continue;    
                    if (i==9 && check_cross(visited, 8)) continue;
                }
                else if (last == 8) {
                    if (i==2 && check_cross(visited, 5)) continue;
                }
                else if (last == 9) {
                    if (i==1 && check_cross(visited, 5)) continue;
                    if (i==3 && check_cross(visited, 6)) continue;    
                    if (i==7 && check_cross(visited, 8)) continue;
                }                 
                res += DFS(s-1, i, (visited|(1<<i)));                 
            }
        }        
        status[code] = res;
        return(res);
    }
    
public:
    int numberOfPatterns(int m, int n) {                   
        int res = 0;        
        for (int i=m;i<=n;i++) {                 
            status.clear();
            res = res + DFS(i,0,0);        
        }
        return(res);        
    }
};