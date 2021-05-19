class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        d = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                w = word[:i]+'*'+word[i+1:]
                d[w].append(word)                
        visited = set([beginWord])
        q = [(beginWord,1)]
        for word, s in q:            
            for i in range(len(word)):
                w = word[:i]+'*'+word[i+1:]
                for ww in d[w]:
                    if ww == endWord:
                        return(s+1) 
                    if ww not in visited:
                        q.append((ww,s+1))
                        visited.add(ww)
        return 0