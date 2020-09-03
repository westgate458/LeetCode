class Solution {
public:
	// simple hash table for unique elements
    int distributeCandies(vector<int>& candies) {
        set<int> k;
        for (auto c : candies) k.insert(c);        
        return(min(k.size(), candies.size()/2));        
    }
};