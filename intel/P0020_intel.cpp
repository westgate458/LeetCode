class Solution {
public:
    bool isValid(string s) {
        stack<char> t;        
        for (char c : s) {            
            if ((c=='(')||(c=='{')||(c=='[')) t.push(c);
            else {
                if (t.size()==0) return false;
                else if (c==')') {
                    if (t.top()=='(') t.pop();
                    else return false;
                }
                else if (c==']') {
                    if (t.top()=='[') t.pop();
                    else return false;
                }
                else if (c=='}') {
                    if (t.top()=='{') t.pop();
                    else return false;
                }                
            }                
        }
        return (t.size()==0);        
    }
};