class Solution {
public:
    int smallestCommonElement(vector<vector<int>>& mat) {
        unordered_map<int, int> hash;
        int rows = mat.size();        
        for (auto row:mat) {
            for (int n:row) {
                hash[n] ++;                
            }           
        }        
        int res = INT_MAX;
        for( const auto& [key, value] : hash ) {
            if ((value==rows)&(key<res)) {
                res = key;
            }            
        }
        if (res == INT_MAX) {
            return(-1);            
        }
        else {
            return(res);
        }
        
    }
};