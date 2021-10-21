class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        users = defaultdict(list)
        
        l = len(timestamp)
        
        idx = [i for _, i in sorted(zip(timestamp,range(l)))]
        
        username = [username[i] for i in idx]
        website = [website[i] for i in idx]
                
        for user, web in zip(username, website):           
            users[user].append(web)
       
        patterns = defaultdict(int)
        for user in users:
            l = len(users[user])
            visited = set()
            for i in range(l):
                for j in range(i+1,l):
                    for k in range(j+1,l):
                        if (users[user][i],users[user][j],users[user][k]) in visited: continue
                        patterns[(users[user][i],users[user][j],users[user][k])] += 1
                        visited.add((users[user][i],users[user][j],users[user][k]))
                        
        max_score = max(patterns.values())
        pattern = [p for p in patterns if patterns[p]==max_score]       
        return(sorted(pattern)[0])
        