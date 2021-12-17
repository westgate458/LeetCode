class Solution(object):
    def wordsTyping(self, sentence, rows, cols):
        """
        :type sentence: List[str]
        :type rows: int
        :type cols: int
        :rtype: int
        """        
        ls = [len(w) for w in sentence]        
        total_l = sum(ls) + len(sentence)   
        cols_available = cols        
        n_total, n_lines = 0, 0
        while n_lines < rows:
            n_lines += 1            
            n_total += cols_available//total_l
            remaining_spaces = cols_available%total_l 
            space_remain_next_line = 0             
            cols_available = cols
            if remaining_spaces >= ls[0]:
                spaces_used = 0                
                for l in ls:                   
                    if spaces_used + l <= remaining_spaces:
                        spaces_used = spaces_used + l + 1
                    else: 
                        break                    
                if spaces_used > 0:
                    n_total += 1
                    space_remain_next_line = total_l-spaces_used                        
                    cols_available = cols - space_remain_next_line
        if space_remain_next_line: n_total -= 1   
        return n_total