class Solution {
public:
	//avoid consecutive ones
    bool canPlaceFlowers(vector<int>& flowerbed, int n) {
        
        flowerbed.insert(flowerbed.begin(), 0);
        flowerbed.push_back(0);        
        
        int i = 1;
        while ((n > 0) && (i < flowerbed.size()-1)) {
            if (flowerbed[i] == 0) {
                if ((flowerbed[i-1] == 0) && (flowerbed[i+1] == 0)) {
                    i ++;
                    n --;                    
                }            
            }
            i ++;  
        }
        return (n==0);
    }
};