class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        aa, bb = a.split('+'), b.split('+')
        a_r, a_i, b_r, b_i = int(aa[0]), int(aa[1][:-1]), int(bb[0]), int(bb[1][:-1])
        return('%d+%di'%(a_r * b_r - a_i * b_i,a_i * b_r + a_r * b_i))