class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        
        number of moves needed = x = m+n-2
        possible path using all x = x!
        res = x! / (m-1)! (n-1)!
        
        """
        
        m, n = m-1, n-1
        total = m+n
        
        bigger = max((m,n))
        smaller = n if bigger == m else m
        res = 1
        
        for i in range(total, bigger, -1):
            res = res * i
        
        for j in range(2, smaller+1):
            res = res // j
            
        return res