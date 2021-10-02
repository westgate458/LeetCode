class Solution {
public:
    bool canCross(vector<int>& stones) {        
        int l = stones.size();        
        if ((l>1)&&(stones[1]>1)) return(false);        
        unordered_map<int,unordered_set<int>> steps;
        unordered_set<int> stone_hash;
        for (int i=1;i<l;i++) stone_hash.insert(stones[i]);         
        steps[1].insert(1);
        int next_step;
        for (int i=1;i<l;i++) {
            for (int k : steps[stones[i]]) {     
                for (int kk=k-1;kk<=k+1;kk++) {
                    if (kk<0) continue;
                    next_step = stones[i]+kk;  
                    if (next_step == stones[l-1]) return(true);                                  
                    if (stone_hash.find(next_step) != stone_hash.end()) {                        
                        steps[next_step].insert(kk);                
                    }                    
                }
                
            }
        } 
        return(false);       
    }
};