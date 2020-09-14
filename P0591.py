class Solution(object):
    def isValid(self, code):
        """
        :type code: str
        :rtype: bool
        """
		# if-else and stacks
        if code[0] != '<': return False
        i = 0
        TAGS = []
        while i < len(code):             
            if code[i] == '<':                
                if code[i:i+9] == '<![CDATA[':
                    if not TAGS: return False
                    while (i <= len(code)) and (code[i-2:i+1] != ']]>'): i += 1 
                else:
                    TAG_NAME = ''
                    i += 1
                    while (i < len(code)) and (code[i] != '>'):
                        if not (code[i] == '/' or 'A' <= code[i] <= 'Z'): return False
                        TAG_NAME += code[i]
                        i += 1                      
                    if TAG_NAME: 
                        if (TAG_NAME[0] == '/'):
                            if not (2 <= len(TAG_NAME) <= 10): return False
                            if (TAGS and (TAG_NAME[1:] == TAGS[-1])):
                                TAGS.pop()                                
                                if (not TAGS) and (i < len(code)-1): return False
                            else:
                                return False
                        else:
                            if not (1 <= len(TAG_NAME) <= 9): return False
                            TAGS.append(TAG_NAME)
                    else: return False
            i += 1        
        return (not TAGS)