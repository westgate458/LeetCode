class Solution {
public:
// start from two ends, try deleting when mismatch found
    bool validPalindrome(string s) {        
        int i = 0, j = s.size()-1;
        bool flag = false;
        while (i<j) {            
            if (s[i]==s[j]) {
                i ++; 
                j --;                    
            }
            else {
                if (flag) return false;                
                if (i+1==j) return true;               
                if (i+2==j) return ((s[i]==s[i+1]) || (s[j]==s[j-1]));                  
                
                if ((s[i+1] == s[j]) && (s[i+2] == s[j-1]) && (s[i+3] == s[j-2])) {
                    flag = true; 
                    i += 4;
                    j -= 3;
                }
                else if ((s[i] == s[j-1]) && (s[i+1] == s[j-2]) && (s[i+2] == s[j-3])) {
                    flag = true;
                    i += 3;
                    j -= 4;
                }                
                else return false;                
            }
        } 
        return true;
    }
};