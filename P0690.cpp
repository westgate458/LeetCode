/*
// Definition for Employee.
class Employee {
public:
    int id;
    int importance;
    vector<int> subordinates;
};
*/

class Solution {
public:
	// DFS from the given node
    int getImportance(vector<Employee*> employees, int id) {        
        unordered_map<int, Employee*> map;        
        for (int i=0;i<employees.size();i++) map[employees[i]->id] = employees[i];        
        queue<int> q;
        q.push(id);
        int res = 0;
        while (q.size()!=0) {            
            int n = q.front();
            q.pop();                       
            res += map[n]->importance;
            for (int nn:map[n]->subordinates) q.push(nn);                       
        }
        return res;
    }
};