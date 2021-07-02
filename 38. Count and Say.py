class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1: return '1'
        s, res = self.countAndSay(n-1), ""
        l = r = 0
        for i, c in enumerate(s):
            if len(s)-1 == i or c != s[i+1]:
                res = res + str(r-l+1) + c 
                l = i + 1
            r += 1
        return res