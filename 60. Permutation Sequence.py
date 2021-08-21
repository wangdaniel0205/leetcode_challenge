class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """

        def factorial(x):
            val = 1
            for i in range(2,x+1):
                val = val*i
            return val
        
        def recursion(candidates, k, n, res):
            if n == 1: return res + candidates[0]
            
            
            fac = factorial(n-1)
            pos = (k-1) // fac
            if pos >= len(candidates):
                res = res + candidates.pop(-1)
            else:
                res = res + candidates.pop(pos)
        
            return recursion(candidates, k-pos*fac, n-1, res)
            
        
    
        return recursion([str(i) for i in range(1, n+1)], k, n, "")