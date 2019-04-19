# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 21:15:55 2019

@author: westg
"""

class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """       
         
        s = [[beginWord]]   
        visited = set([beginWord])
        letters = 'abcdefghijklmnopqrstuvwxyz'     
        
        flag = False
        c = len(wordList)
    
        while not flag and s and c > 0:
            s_new = []
            visited_new = set([])
            c = c - 1
            for i in range(len(s)):
                word = s[i][-1]
                
                for j in range(len(word)):
                    for ch in letters:
                        new_word = word[:j] + ch + word[j+1:]
                        if (new_word in wordList) and (not (new_word in visited)):
                            flag = flag or new_word == endWord
                            s_new.append(s[i] + [new_word])
                            visited_new.add(new_word)
            s = s_new
            visited |= visited_new
        
        return [ans for ans in s if ans[-1] == endWord]

beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]    

#beginWord = "hit"
#endWord = "cog"
#wordList = ["hot","dot","dog","lot","log"]
test = Solution()
print test.findLadders(beginWord, endWord, wordList)
                
            
                    