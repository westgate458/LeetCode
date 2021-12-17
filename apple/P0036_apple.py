class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(9):
            s = set()
            for j in range(9):
                if board[i][j] != '.' and board[i][j] in s:
                    return False
                else:
                    s.add(board[i][j])
                    
        for j in range(9):
            s = set()
            for i in range(9):
                if board[i][j] != '.' and board[i][j] in s:
                    return False
                else:
                    s.add(board[i][j])
                    
        for i in [1,4,7]:
            for j in [1,4,7]:
                s = set()
                for ii,jj in [(i-1,j-1),(i-1,j),(i-1,j+1),
                            (i,j-1),(i,j),(i,j+1),
                            (i+1,j-1),(i+1,j),(i+1,j+1)]:
                    if board[ii][jj] != '.' and board[ii][jj] in s:
                        return False
                    else:
                        s.add(board[ii][jj])
          
        return True