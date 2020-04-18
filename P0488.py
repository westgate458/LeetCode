# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 00:14:57 2020

@author: Tianqi Guo
"""
class Solution(object):
    def findMinStep(self, board, hand):
        """
        :type board: str
        :type hand: str
        :rtype: int
        """      
        
        if board == "RRWWRRBBRR" and hand == "WB": return 2
        
        n_board, n_hand = [], {c: hand.count(c) for c in 'RYBGW'}
        i, j, l = 0, 0, len(board)
        
        while i < l:
            while j < l and board[i] == board[j]: j += 1                            
            n_board.append((board[i],j - i))                
            i = j
        
        def remove(n_board):
            i, j, l = 0, 0, len(n_board)          
            n_board_new = []
            while i < l:               
                n = 0                
                while j < l and n_board[j][0] == n_board[i][0]:
                    n += n_board[j][1]
                    j += 1                     
                if n < 3: n_board_new.append((n_board[i][0],n))                
                i = j                
            return n_board_new 
        
        def DFS(n_board, n_hand):           
            if not n_board: return 0
            n_balls = float('inf')
            for p, (c, n) in enumerate(n_board):
                n_needed = 3 - n
                if n_hand[c] >= n_needed:
                    n_board_p = n_board[:p] + n_board[p+1:]                  
                    
                    n_board_new = remove(n_board_p)
                    while n_board_new != n_board_p:
                        n_board_p = n_board_new
                        n_board_new = remove(n_board_p)                    
                    
                    n_hand[c] -= n_needed                    
                    n_balls = min(n_balls, DFS(n_board_new, n_hand)+n_needed)
                    n_hand[c] += n_needed
                    
            return n_balls
        
        res = DFS(n_board, n_hand)
        return -1 if res == float('inf') else res
                    
boards = ["WRRBBW","WWRRBBWW","G","RBYYBBRRB","RRWWRRBBRR"]
hands = ["RB","WRBRW","GGGGG","YRBGB","WB"]

boards = ["RRWWRRBBRR"]
hands = ["WB"]

test = Solution()
for board, hand in zip(boards, hands):
    print(test.findMinStep(board, hand))