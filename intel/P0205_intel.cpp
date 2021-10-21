class Solution {
public:
    bool isIsomorphic(string s, string t) {        
        unordered_map<char,char> m1, m2;   
        bool available_1, available_2;           
        for (int i=0;i<s.size();i++) {  
            available_1 = (m1.find(s[i]) == m1.end());
            available_2 = (m2.find(t[i]) == m2.end());            
            if ((available_1) and (available_2)) {
                m1[s[i]] = t[i];
                m2[t[i]] = s[i];
            }
            else if (((not available_1) and (not available_2)) and (((m1[s[i]] == t[i]) and (m2[t[i]] == s[i])))) continue;                
            else return(false);            
        }        
        return(true);        
    }
};