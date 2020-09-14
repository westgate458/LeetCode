class Solution {
public:
	// hashtable for index in first list
    vector<string> findRestaurant(vector<string>& list1, vector<string>& list2) {
        unordered_map<string,int> inds;
        for (int i = 0; i < list1.size(); i ++){
            inds[list1[i]] = i;
        }
        vector<string> res;
        int sum = 2000;        
        for (int i = 0; i < list2.size(); i ++){
            if (inds.find(list2[i]) != inds.end()){
                if (inds[list2[i]] + i == sum) {
                    res.push_back(list2[i]);                    
                }
                else if (inds[list2[i]] + i < sum) {
                    sum = inds[list2[i]] + i;
                    res = {list2[i]};
                }
            }
        }
        return res;
    }
};