class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
		# floodfill from the given seed
        r, c = click
        if board[r][c] == 'M':
            board[r][c] = 'X' 
        else:
            m, n = len(board), len(board[0])
            q = [(r,c)]
            while q:
                r, c = q.pop()
                n_mines = 0
                qq = []
                for rr, cc in [(r+1,c),(r-1,c),(r,c-1),(r,c+1),(r+1,c+1),(r+1,c-1),(r-1,c-1),(r-1,c+1)]:
                    if 0 <= rr < m and 0 <= cc < n:
                        if board[rr][cc] == 'M':
                            n_mines += 1
                        elif board[rr][cc] == 'E':
                            qq.append((rr,cc))
                if n_mines == 0:
                    board[r][c] = 'B'
                    q += qq                            
                else:
                    board[r][c] = str(n_mines)
        return board
                    
                        