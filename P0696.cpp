class Solution {
public:
    int countBinarySubstrings(string s) {        
        //ios_base::sync_with_stdio(0); cin.tie(0);
        int i = 0, res = 0, pre = 0, l = s.size();  
        for (int j=0;j < l;j++) {
            if (s[i]!=s[j]) {             
                res += min(pre,j-i);     
                pre = j - i;
                i = j;
            }            
        }           
        return res+min(pre,l-i);        
    }
};