class Solution {
public:
    bool canTransform(string start, string end) {
        int i = 0, n = start.size(); 
        int j, k, p;       
        while (i<n) {
            if (start[i]==end[i]) i ++;  
            else if ((start[i]=='X')&&(end[i]=='L')) {
                j = i;
                k = 0;
                p = -1;
                while ((j<n)&&(start[j]!='R')&&(end[j]!='R')&&(k<=0)) {
                    if (start[j]=='L') k ++;
                    if (end[j]=='L') k --;
                    if (k==0) p = j;                    
                    j ++;
                }                
                if (p==-1) return false;
                i = p+1;                    
            }
            else if ((start[i]=='R')&&(end[i]=='X')) {
                j = i;
                k = 0;
                p = -1;
                while ((j<n)&&(start[j]!='L')&&(end[j]!='L')&&(k>=0)) {
                    if (start[j]=='R') k ++;
                    if (end[j]=='R') k --;
                    if (k==0) p = j;                    
                    j ++;
                }                
                if (p==-1) return false;
                i = p+1;                
            }
            else return false;
        }
        return true;
    }
};