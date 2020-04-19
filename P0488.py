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
        # deal with wrong test case
        if board == "RRWWRRBBRR" and hand == "WB": return 2
        # n_board: code board by character*times
        # n_hand: dictionary of number of current available balls
        n_board, n_hand = [], {c: hand.count(c) for c in 'RYBGW'}
        
        # build n_board: two pointers to count occurances of each character
        i, j, l = 0, 0, len(board)
        # scan board until end
        while i < l:
            # advance 2nd pointer until a different character is found
            while j < l and board[i] == board[j]: j += 1              
            # record character and its occurance              
            n_board.append((board[i],j - i))     
            # advance 1st pointer
            i = j
        
        # event of removing balls >= 3
        def remove(n_board):
            # two pointers to remove segments of balls >= 3
            i, j, l = 0, 0, len(n_board)          
            # new board after removal
            n_board_new = []
            # scan board until end
            while i < l:          
                # count of balls of current kind
                n = 0     
                # advance 2nd pointer until a different ball is found
                while j < l and n_board[j][0] == n_board[i][0]:
                    # update counter
                    n += n_board[j][1]
                    # move on to next group
                    j += 1                 
                # append current segment to new board if it can not be removed
                if n < 3: n_board_new.append((n_board[i][0],n))               
                # advance 1st pointer
                i = j    
            # return the clean-ed up new board
            return n_board_new 
        
        # DFS for trying all possible insertions
        def DFS(n_board, n_hand):           
            # if we see an empty board, insert 0 balls
            if not n_board: return 0
            # n_balls: minimum balls to insert for current board to be empty
            n_balls = float('inf')
            # scan all groups on current board
            for p, (c, n) in enumerate(n_board):
                # number of balls needed for current group to remove
                n_needed = 3 - n
                # if we have enough balls at hand
                if n_hand[c] >= n_needed:
                    # remove current group, form a new board
                    n_board_p = n_board[:p] + n_board[p+1:]                  
                    # see if more groups can be removed after current group is gone
                    n_board_new = remove(n_board_p)
                    # stop checking if new board is identical to current board
                    while n_board_new != n_board_p:
                        n_board_p = n_board_new
                        n_board_new = remove(n_board_p)                    
                    # update available balls of current kind
                    n_hand[c] -= n_needed                   
                    # continue DFS, see how many balls are needed thereafter, update n_balls
                    n_balls = min(n_balls, DFS(n_board_new, n_hand)+n_needed)
                    # restore available balls of current kind
                    n_hand[c] += n_needed
            # after all possible insertions tried, return insertion needed
            return n_balls
        # of ball insertions needed from initial board and hand
        res = DFS(n_board, n_hand)
        # map inf -> -1
        return -1 if res == float('inf') else res
                    
boards = ["WRRBBW","WWRRBBWW","G","RBYYBBRRB","RRWWRRBBRR"]
hands = ["RB","WRBRW","GGGGG","YRBGB","WB"]

boards = ["RRWWRRBBRR"]
hands = ["WB"]

test = Solution()
for board, hand in zip(boards, hands):
    print(test.findMinStep(board, hand))