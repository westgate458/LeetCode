class Solution {
public:
    bool canConvert(string str1, string str2) {
        unordered_map<char,char> m;        
        int l = str1.size();        
        unordered_set<char> s;        
        for (int i = 0;i<l;i++) {
            s.insert(str2[i]);
            if (m.find(str1[i])==m.end()) m[str1[i]] = str2[i];
            else if (m[str1[i]] != str2[i]) return(false);
        }
        if ((m.size()<26)|(s.size()<26)) return(true);
        else {  
            unordered_set<char> visited;
            char n;
            for (char c:"abcdefghijklmnopqrstuvwxyz") {
                visited.clear();
                n = c;
                while (visited.find(n)==visited.end()) {
                    visited.insert(n);
                    n = m[n];
                }
                if (visited.size()>1) return false;
            }
        }
        return(true);
    }
};