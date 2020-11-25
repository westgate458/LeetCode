class Solution {
public:
    bool hasAlternatingBits(int n) {
        int d = n & 1;
        int dd = 0;
        while (n!=0) {            
            n >>= 1;            
            dd = n & 1;           
            if (dd==d) return false;                     
            d = dd;            
        }
        return true;
    }
};