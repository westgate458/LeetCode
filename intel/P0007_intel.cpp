class Solution {
public:
    int reverse(int x) {
        double res = 0;        
        int d = 0;
        while (x!=0) {            
            d = x%10;
            res = res*10+d;
            x = x/10;                     
        }
        if ((res<-pow(2,31))||(res>pow(2,31)-1)) return(0);
        return res;
    }
};