class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        res, line, width = [], [], 0        
        for word in words: 
            if len(word) + width > maxWidth:
                if len(line) == 1:                    
                    res.append(line[0]+' '*(maxWidth-len(line[0])))                        
                else:  
                    spaces_perSlot, spaces_extra = divmod(maxWidth - sum([len(w) for w in line]),len(line)-1)                
                    if spaces_extra:
                        res.append((' '*(spaces_perSlot+1)).join(line[:spaces_extra]) + ' '*(spaces_perSlot+1) + (' '*spaces_perSlot).join(line[spaces_extra:]))  
                    else:
                        res.append((' '*spaces_perSlot).join(line[spaces_extra:]))
                line, width = [], 0        
            width += len(word) + 1
            line.append(word) 
        lastLine = ' '.join(line)
        res.append(lastLine+' '*(maxWidth-len(lastLine)))
        return res
        
                
            