class Solution {
public:
    string reverseWords(string s) {
        //basic string manipulation
        int i = 0;        
        int j;
        s = s + ' ';
        for (int k = 0; k < s.length(); k++) {
            if (s[k] == ' ') {
                j = k - 1;
                while (i < j) {
                    swap(s[i],s[j]);
                    i ++;
                    j --;
                }
                i = k + 1;
            }  
        }
        return s.substr(0,s.length()-1);
    }
};