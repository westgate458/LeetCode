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
        
        # deal with trivial case
        if endWord not in wordList:
            return []
        
        # length of each word
        wl = len(beginWord)
        
        # dictionary storing all intermediate words
        # which are formed by replacing each character in words by '*'
        intermediate_words = defaultdict(set)  
        # for each word in word list
        for word in wordList:
            # replace each character in words by '*'
            for i in range(wl):
                # add current word to the entry of the intermediate word
                intermediate_words[word[:i]+'*'+word[i+1:]].add(word)           
        
        # flag if the end word has been found
        flag = False
        # word set for current level, which has the same distance from begin word
        s = set([beginWord])   
        # mark visited words to avoid going backwards
        visited = set([beginWord])        
        # all nodes from previous level that leads to current word
        parent_nodes = defaultdict(set)               
        
        # continue traversing until end word is found or no word is on current level
        while not flag and s:
            
            # word set for next level
            s_new = set()
            # word already visited for next level to avoid duplicates
            visited_new = set()
            
            # for each word on current level
            for word in s:                
                # find the intermediate words
                for j in range(wl):          
                    # for all words that share the same intermediate word with current word
                    # i.e. distance of 1 from current word
                    for new_word in intermediate_words[word[:j]+'*'+word[j+1:]]:
                        # if this word has not been visited on previous levels, 
                        # but could have already been placed on the next level
                        if new_word not in visited:
                            # check if have reached end word 
                            flag = flag or new_word == endWord
                            # mark this word already visited for next level
                            visited_new.add(new_word)
                            # add current word as the parent word for the new word
                            parent_nodes[new_word] |= set([word])  
                            # add the new word to next level
                            s_new |= set([new_word])                     
            # move on to next level
            s = s_new
            # update the overall visited words
            visited |= visited_new
        
        # dfs to create paths from end word
        def path_const(word):
            # if have reached begin word
            if word == beginWord:
                # form and return a new path
                return [[beginWord]]
            
            # all paths going via current node
            paths = []
            # for all parent nodes that go before current node
            for parent in parent_nodes[word]:
                # find all paths go via each parent node
                # and gather those paths
                paths +=  path_const(parent)            
            # add current word to all the parent paths and return to next level
            return [path + [word] for path in paths]
        
        # construct paths from the endword
        return path_const(endWord) 
        

beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]    

#beginWord = "hit"
#endWord = "cog"
#wordList = ["hot","dot","dog","lot","log"]
test = Solution()
print test.findLadders(beginWord, endWord, wordList)
