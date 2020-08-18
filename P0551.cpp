//basic string manipulation
class Solution {
public:
    bool checkRecord(string s) {        
        int n_A = 0;
        int n_L = 0;        
        for (char c : s) {
            if (c == 'L') {
                if (n_L == 2) return false;               
                else n_L ++;    
            }
            else {
                n_L = 0; 
                if (c == 'A') {
                    n_A++;  
                    if (n_A == 2) return false;                   
                }                
            }            
        }     
        return true;
    }
};