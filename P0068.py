# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 17:42:47 2019

@author: Tianqi Guo
"""

words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"]
maxWidth = 20

n_words = len(words)

paragraph = []
f_word = 0
l_word = -1

while l_word < n_words-1:

    width_total = -1
    width_words = 0    
    
    line = ''    
    
    while (l_word < n_words-1) and (width_total + 1 + len(words[l_word+1]) <= maxWidth):
        width_total = width_total + 1 + len(words[l_word+1])
        width_words = width_words + len(words[l_word+1])
        l_word = l_word + 1   
    
    new_spaces = int(maxWidth - width_words)
    new_words = l_word - f_word + 1
    
    if new_words == 1:
        line = line + words[l_word] + ' ' * new_spaces
    else:
        if l_word == n_words-1:
            spaces = [1] * (new_words-1) + [new_spaces - new_words + 1]
        else:   
            new_space = new_spaces//(new_words-1)
            extra_space = new_spaces - new_space*(new_words-1)            
            spaces = [new_space] * (new_words-1) + [0]
            spaces = [spaces[x] + 1 for x in range(extra_space)] + spaces[extra_space:]
        line = line + ''.join(words[f_word+x] + ' '*spaces[x] for x in range(0,new_words))
   
    paragraph.append(line)    
    f_word = l_word + 1

