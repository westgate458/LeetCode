class Solution(object):
    def minStickers(self, stickers, target):
        """
        :type stickers: List[str]
        :type target: str
        :rtype: int
        """  
        def DFS(remains): 
            if remains not in self.dp:                
                self.dp[remains] = float('inf')  
                for i, c in enumerate(remains):
                    if c > 0:                    
                        for sticker_id in to_stickers[i]:                        
                            self.dp[remains] = min(self.dp[remains], DFS(tuple([max(a-b,0) for a,b in zip(remains,counts[sticker_id])]))+1) 
                        break            
            return self.dp[remains]
        
        target_c = Counter(target)   
        needs = []
        to_stickers = [[] for _ in range(len(target_c))]
        for i, c in enumerate(target_c):            
            needs.append(target_c[c])
            target_c[c] = i        
        counts = []
        id = -1
        for sticker in stickers:
            count = [0]*len(needs)
            for c in sticker:
                if c in target_c:
                    count[target_c[c]] += 1 
            for pre_count in counts:
                if all([a<=b for a,b in zip(count, pre_count)]):
                    count = []
                    break
            if count:
                id += 1                
                for i, c in enumerate(count):
                    if c > 0: to_stickers[i].append(id)
                counts.append(count)        
        if any([i == [] for i in to_stickers]): return -1
        self.dp = {tuple([0]*len(needs)):0}
        return DFS(tuple(needs))