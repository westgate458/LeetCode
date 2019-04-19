# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 21:15:55 2019

@author: Tianqi Guo
"""

from collections import defaultdict
class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """       
        if endWord not in wordList:
            return []
        
        wl = len(beginWord)
        
        intermediate_words = defaultdict(set)        
        for word in wordList:
            for i in range(wl):
                intermediate_words[word[:i]+'*'+word[i+1:]].add(word)           
                        
        flag = False
        s = set([beginWord])   
        visited = set([beginWord])        
        parent_nodes = defaultdict(set)               
    
        while not flag and s:
            s_new = set()
            visited_new = set()
           
            for word in s:                
                for j in range(wl):                                  
                    for new_word in intermediate_words[word[:j]+'*'+word[j+1:]]:
                        if new_word not in visited:
                            flag = flag or new_word == endWord
                            visited_new.add(new_word)
                            parent_nodes[new_word] |= set([word])  
                            s_new |= set([new_word])                     
            s = s_new
            visited |= visited_new
            
        def path_const(word):
            if word == beginWord:
                return [[beginWord]]
            paths = []
            for parent in parent_nodes[word]:
                paths +=  path_const(parent)            
            return [path + [word] for path in paths]
        
        return path_const(endWord) 
        

beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]    

#beginWord = "hit"
#endWord = "cog"
#wordList = ["hot","dot","dog","lot","log"]
test = Solution()
print test.findLadders(beginWord, endWord, wordList)
