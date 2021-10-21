class LRUCache {
public:
    
    int cap;
    
    list<int> LRUList; // keys, recent in front, old in back 
    
    unordered_map<int, list<int>::iterator> LRUMap; // key -> pointer in LRUList
    unordered_map<int, int> values; // key -> value    
    
    LRUCache(int capacity) {
        cap = capacity;        
    }
    
    int get(int key) {        
        
        if (values.find(key)!=values.end()) {
            
            LRUList.erase(LRUMap[key]);
            LRUList.push_front(key);
            LRUMap[key] = LRUList.begin();
            
            return(values[key]);
            
        }
        
        return(-1);
    }
    
    void put(int key, int value) {
        
        if (values.find(key)!=values.end()) {            
            LRUList.erase(LRUMap[key]);
            LRUList.push_front(key);
            LRUMap[key] = LRUList.begin();    
            values[key] = value;            
        }
        else {
            if (values.size() == cap) {
                LRUMap.erase(LRUList.back());
                values.erase(LRUList.back());
                LRUList.pop_back();
            }
            LRUList.push_front(key);
            LRUMap[key] = LRUList.begin();    
            values[key] = value;  
        }           
                    
    } 
    
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */