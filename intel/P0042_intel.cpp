class Solution {
public:
    int trap(vector<int>& height) {        
        int max_left = 0, max_right = 0, j = height.size() - 1, i = 0, res = 0;
        while (i<=j) {
            if (max_left <= max_right) {
                if (height[i] > max_left) {
                    max_left = height[i];
                }
                else {
                    res += (max_left - height[i]);                     
                }
                i ++;
            }
            else {
                if (height[j] > max_right) {
                    max_right = height[j];
                }
                else {
                    res += (max_right - height[j]);                     
                }
                j --;
            }
            
        }      
        return(res);
    }
};