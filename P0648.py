class Solution(object):
    def replaceWords(self, dictionary, sentence):
        """
        :type dictionary: List[str]
        :type sentence: str
        :rtype: str
        """
		# using Trie (Prefix Tree)  
        d = {}       
        
        for word in dictionary:
            node = d
            for c in word:
                if 'isWord' in node:                    
                    break
                elif c not in node:                
                    node[c] = {}              
                node = node[c]
            node['isWord'] = True
        
        def replace(word):
            node = d            
            for j, c in enumerate(word):                  
                if c not in node:
                    return word                       
                else:
                    node = node[c]
                if 'isWord' in node:                    
                    return word[:j+1]
            return word

        return(' '.join(map(replace, sentence.split(' '))))
                
            
            
        