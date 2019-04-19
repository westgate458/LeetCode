# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 21:15:55 2019

@author: Tianqi Guo
"""
from collections import defaultdict
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """       
        
        if endWord not in wordList:
            return 0
        
        intermediate_words = defaultdict(list)
        wl = len(beginWord)
        for word in wordList:
            for i in range(wl):
                intermediate_words[word[:i]+'*'+word[i+1:]].append(word)      
        
        s = [beginWord]   
        wordSet = set(wordList)
     
        c = 1
        while s:
            s_new = []            
            c = c + 1
            for i in range(len(s)):                           
                for j in range(wl):                                  
                    for new_word in intermediate_words[s[i][:j]+'*'+s[i][j+1:]]:
                        if new_word == endWord:
                            return c
                        if new_word in wordSet:                            
                            s_new.append(new_word)
                            wordSet.remove(new_word)
            s = s_new
            
        return 0

beginWord = "hog"
endWord = "cog"
wordList = ["cog"]

#beginWord = "hit"
#endWord = "cog"
#wordList = ["hot","dot","dog","lot","log","cog"]    

#beginWord = "hit"
#endWord = "cog"
#wordList = ["hot","dot","dog","lot","log"]

test = Solution()
print test.ladderLength(beginWord, endWord, wordList)
                
            
                    