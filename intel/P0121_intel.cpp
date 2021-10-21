class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int lowest = 10000;
        int res = 0;
        for (int p : prices) {
            if (p-lowest>res) res = p-lowest;           
            if (p<lowest) lowest = p;
        }
        return(res);
    }
};