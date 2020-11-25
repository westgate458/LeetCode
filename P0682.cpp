class Solution {
public:
	//simple stack
    int calPoints(vector<string>& ops) {
        vector<int> s; 
        for (auto c : ops) {
            if (c=="+") s.push_back(s[s.size()-1]+s[s.size()-2]);  
            else if (c=="D") s.push_back(s[s.size()-1]*2);
            else if (c=="C") s.pop_back(); 
            else s.push_back(stoi(c));           
        }        
        int res = 0;
        for (auto n:s) res += n;
        return res;
    }
};