class DinnerPlates {

private:
    int cap;
    vector<stack<int>> racks;    
    priority_queue<int> right_most;
    priority_queue<int,vector<int>,greater<int>> left_most;
    
    
public:
    DinnerPlates(int capacity) {
        cap = capacity;         
    }
    
    void push(int val) {        
                
        bool flag = true;
        
        while (flag&&(left_most.size()>0)) {
            int i = left_most.top();
            left_most.pop();
            if (racks[i].size()<cap) {
                racks[i].push(val);
                left_most.push(i);
                flag = false;
            }
            if (racks[i].size()>0) {
                right_most.push(i);
            }            
        }
        
        if (flag) {
            racks.push_back(stack<int>());            
            racks[racks.size()-1].push(val);
            if (racks[racks.size()-1].size()<cap) {
                left_most.push(racks.size()-1);
            }            
            right_most.push(racks.size()-1);
        }
        
    }
    
    int pop() {           
        
        while (right_most.size()>0) {
            int i = right_most.top();
            right_most.pop();           
            if (racks[i].size()>0) {
                int val = racks[i].top();
                racks[i].pop();
                if (racks[i].size()>0) {
                    right_most.push(i);
                }  
                left_most.push(i);               
                return(val);
            }            
        }            
        return(-1);        
    }
    
    int popAtStack(int index) {
        
        if ((racks.size()>index)&&(racks[index].size()>0)) {
            int val = racks[index].top();
            racks[index].pop();
            left_most.push(index);              
            
            return val;
        }       
        return(-1);        
    }
};

/**
 * Your DinnerPlates object will be instantiated and called as such:
 * DinnerPlates* obj = new DinnerPlates(capacity);
 * obj->push(val);
 * int param_2 = obj->pop();
 * int param_3 = obj->popAtStack(index);
 */