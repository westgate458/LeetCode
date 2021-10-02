class Solution {
        
private:
    
    bool check_possible(vector<int> bloomDay, int k, int m, int d) {
        
        int b = 0, c = 0;  
        for (int j = 0; j < bloomDay.size(); j ++) {
            if (bloomDay[j]<=d) c ++;          
            else {                
                b += c/k;
                c = 0;
            }
        }
        b += c/k;       
        if (b>=m)  return true; 
        return(false);        
    }
    
    
public:
    int minDays(vector<int>& bloomDay, int m, int k) {
        if(bloomDay.size() < m*k) return -1; 
        int i = INT_MAX, j = INT_MIN;
        for(auto o : bloomDay) {
            i = min(i ,o);
            j = max(j, o);
        }  
        while (i<j) {
            int mid = (i+j)/2;
            if (check_possible(bloomDay, k, m, mid)) j = mid;            
            else i = mid + 1;
        }                      
        return(i);
    }
};