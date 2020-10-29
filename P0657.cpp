class Solution {
public:
	// count number of each moves
    bool judgeCircle(string moves) {
        int h = 0, v = 0;        
        for (auto c : moves) {
            if (c=='U') v++;            
            else if (c=='D') v--;
            else if (c=='L') h++;
            else if (c=='R') h--;            
        }
        return ((h==0)&&(v==0));
    }
};