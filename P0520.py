class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """ 
        return len(word) == 1 or word[1:].islower() or word.isupper()