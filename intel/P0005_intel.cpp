class Solution {
public:
    string longestPalindrome(string s) {
        
        int res = 0;
        int l = s.size();
        string str;
        
        for (int i=0;i<l;i++) {            
            for (int m=i;m>=0;m--) {                
                int n = 2*i-m;
                if ((n >= l)||(s[m]!=s[n])) break;  
                if (n-m+1>res) {
                    res = n-m+1;
                    str = s.substr(m,res);                    
                }                
            }
        }
        
        for (int i=0;i<l-1;i++) {            
            for (int m=i;m>=0;m--) {                
                int n = 2*i-m+1;
                if ((n >= l)||(s[m]!=s[n])) break;               
                if (n-m+1>res) {
                    res = n-m+1;
                    str = s.substr(m,res);                    
                }                
            }
        }
        
        return str;
    }
};