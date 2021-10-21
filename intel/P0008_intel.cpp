class Solution {
public:
    int myAtoi(string s) {
        int sign = 0;
        double res = 0;
        bool started = false;
        string chrs = "0123456789";
        
        for (char c : s) {
            auto pos = chrs.find(c);            
            if (started) {                
                if (pos != string::npos) res = res * 10 + pos;                
                else break;                
            }
            else {
                if (pos != string::npos) {
                    if (sign == 0) sign = 1;                     
                    started = true;
                    res = res * 10 + pos;
                }
                else {                    
                    if (c==' ') continue;
                    else if (c=='+') {
                        if (sign == 0) {
                            sign = 1; 
                            started = true;
                        }
                        else return(0);
                    }                        
                    else if (c=='-') {
                        if (sign == 0) {
                            sign = -1;
                            started = true;
                        }
                        else return(0);    
                    }
                    else return(0);
                    
                } 
            }
        }
        res = res*sign;
        if (res<-2147483648) res = -2147483648;        
        if (res>2147483647) res = 2147483647;        
        return(int(res));
    }
};

