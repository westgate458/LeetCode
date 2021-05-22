class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        state = board[0]+board[1]
        if state == [1,2,3,4,5,0]: return(0)
        visited = set([tuple(state)])       
        q = [(state,0, state.index(0))]
        next_state = [[1,3],[0,2,4],[1,5],[0,4],[1,3,5],[2,4]]        
        for b, s, i in q:
            for j in next_state[i]:                
                bb = list(b)
                bb[i], bb[j] = bb[j], bb[i]
                if bb == [1,2,3,4,5,0]: return(s+1)
                if tuple(bb) not in visited:
                    q.append((bb,s+1,j))
                    visited.add(tuple(bb))       
        return(-1)