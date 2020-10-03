class Solution {
public:
// check if result is integer
    bool judgeSquareSum(int c) {
        double cc = double(c);
        double b;        
        for (double a = 0; a <= sqrt(cc); a++) {
            b = sqrt(cc - a * a);            
            if (floor(b) == b) return true; 
        }        
        return false;        
    }
};