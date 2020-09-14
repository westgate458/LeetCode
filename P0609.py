class Solution(object):
    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
		# hashtable for content
        d = defaultdict(list)
        for folder in paths:
            files = folder.split(' ')
            for file in files[1:]:
                temp = file.split('(')              
                d[temp[1]] += [files[0]+'/'+temp[0]]
        return([v for v in d.values() if len(v)>1])
        