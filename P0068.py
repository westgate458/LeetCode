# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 17:42:47 2019

@author: Tianqi Guo
"""

class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        
        # number of words
        n_words = len(words)
        
        # answer list
        paragraph = []
        # first and last word indices for current line
        f_word = 0
        l_word = -1
        
        # continue adding lines to the paragraph until the last word
        while l_word < n_words-1:
            
            # width of the current line with spaces
            width_total = -1
            # width of the current line without spaces
            width_words = 0    
                     
            # continue adding words to current line 
            # until the current line exceeds the max width
            while (l_word < n_words-1) and (width_total + 1 + len(words[l_word+1]) <= maxWidth):
                # update the widths with and without spaces for current line
                width_total = width_total + 1 + len(words[l_word+1])
                width_words = width_words + len(words[l_word+1])
                # move on to next word
                l_word = l_word + 1   
            
            # determine how many spaces are needed to pad for max width
            new_spaces = int(maxWidth - width_words)
            # determine how many words are added to current line
            new_words = l_word - f_word + 1
            
            # if only one word is on current line, or the current line is the last line
            if (new_words == 1) or (l_word == n_words-1):
                # no need to do justification, simply pad spaces after the last word                
                spaces = [1] * (new_words-1) + [new_spaces - new_words + 1]
            # if need to do justification
            else:   
                
                # try even distribution of spaces after each word
                new_space = new_spaces//(new_words-1)
                # the last word has no spaces after it
                spaces = [new_space] * (new_words-1) + [0]
                
                # number of extra spaces on the left in case of uneven distribution
                extra_space = new_spaces - new_space*(new_words-1)    
                # put one more space after each word on the left      
                spaces = [spaces[x] + 1 for x in range(extra_space)] + spaces[extra_space:]
            
            # form the line by putting words and spaces together
            line = ''.join(words[f_word+x] + ' '*spaces[x] for x in range(0,new_words))
            # append current line to the paragraph
            paragraph.append(line) 
            # update index for the first word on the next line
            f_word = l_word + 1
        
        # return the justified paragraph
        return paragraph

words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"]
maxWidth = 20
test = Solution()
print test.fullJustify(words, maxWidth)