class Solution(object):
    def tictactoe(self, moves):
        """
        :type moves: List[List[int]]
        :rtype: str
        """
        board = [[0]*3 for _ in range(3)]
        for i in range(len(moves)):           
            board[moves[i][0]][moves[i][1]] = 1 if i%2==0 else -1            
        
        s = board[0][0]+board[1][1]+board[2][2]      
        if s==3: return 'A'
        elif s==-3: return 'B'
        s = board[0][2]+board[1][1]+board[2][0]  
        if s==3: return 'A'
        elif s==-3: return 'B'
        
        for i in range(3):            
            s = board[i][0]+board[i][1]+board[i][2]            
            if s==3: return 'A'
            elif s==-3: return 'B'            
            s = board[0][i]+board[1][i]+board[2][i]    
            if s==3: return 'A'
            elif s==-3: return 'B'        
        
        if len(moves)==9: return('Draw')
        else: return('Pending')