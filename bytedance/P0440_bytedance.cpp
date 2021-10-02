class Solution {
public:    
    int helper(long n, long node) {
        long right = node + 1;
        int count = 0;
        while (node <= n) {           
            count = count + min(right-node,n-node+1); 
            node = node * 10;
            right = right * 10;            
        }       
        return(count);
    }
    
    int findKthNumber(int n, int k) {
        
        int node = 1;
        k = k - 1;
        while (k>0) {            
            int count = helper(n, node);           
            if (k >= count) {
                k -= count;
                node = node + 1;
            }
            else {
                k -= 1;
                node = node *10;
            }
        }        
    return(node);        
    }
};