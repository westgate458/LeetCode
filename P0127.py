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
        
        # deal with trivial case
        if endWord not in wordList:
            return 0
        
        # length of each word
        wl = len(beginWord)
        
        # dictionary storing all intermediate words
        # which are formed by replacing each character in words by '*'
        intermediate_words = defaultdict(list)        
        
        # for each word in word list
        for word in wordList:
            # replace each character in words by '*'
            for i in range(wl):
                # add current word to the entry of the intermediate word
                intermediate_words[word[:i]+'*'+word[i+1:]].append(word)      
        
        # word set for current level, which has the same distance from begin word
        s = [beginWord]   
        # all avialble words that have not been visited
        wordSet = set(wordList)
        
        # distance counter \ ladder length
        c = 1
        # continue traversing until no word is on current level
        while s:
            # word set for next level
            s_new = []    
            # update conter
            c = c + 1
            
            # for each word on current level
            for i in range(len(s)):    
                # find the intermediate words                       
                for j in range(wl):    
                    # for all words that share the same intermediate word with current word
                    # i.e. distance of 1 from current word                              
                    for new_word in intermediate_words[s[i][:j]+'*'+s[i][j+1:]]:
                        # if have reached end word 
                        if new_word == endWord:
                            # return the level counts\ladder length
                            return c
                        # if the new word has not been visited
                        if new_word in wordSet:               
                            # put it on next level
                            s_new.append(new_word)
                            # mark it visited
                            wordSet.remove(new_word)
            # move on to next level
            s = s_new
        
        # if end word has not been reached, there is no desired word ladder
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
                
            
                    