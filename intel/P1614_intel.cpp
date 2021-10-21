class Solution {
public:
    int maxDepth(string s) {        
        int d = 0;
        int res = 0;
        for (char c:s) {
            if (c=='(') {                
                d ++;
                if (d>res) res = d;
            }
            else if (c==')') d--;            
        }
        return(res);
    }
};