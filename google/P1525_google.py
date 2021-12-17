class Solution:
    def numSplits(self, s: str) -> int:
        l, res = len(s), 0        
        left_set, right_set = set(), set()
        left_n, right_n = [0]*l, [0]*l              
        for i in range(l):            
            left_set.add(s[i])
            right_set.add(s[-i-1])
            left_n[i], right_n[-i-1] = len(left_set), len(right_set)                  
        return sum([left_n[i] == right_n[i+1] for i in range(l-1)])