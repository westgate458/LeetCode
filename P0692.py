class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """               
        return([x[0] for x in sorted(Counter(words).items(), key=lambda x:(-x[1],x[0]))[:k]])