class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {                
        for (int l=0;l<strs[0].size();l++) {           
            for (string s:strs) {
                if ((l==s.size())||(s[l]!=strs[0][l])) return(strs[0].substr(0,l));                
            }
        }
        return(strs[0]);        
    }
};