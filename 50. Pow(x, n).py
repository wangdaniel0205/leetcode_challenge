class Solution:
    def myPow(self, x, n):
        # base
        if n == 0: return 1
        elif n == 1: return x
        elif n < 0: return 1.0 / self.myPow(x, -n)
        
        
        # general
        partition = self.myPow(x, n//2)
        if n % 2 == 0:
            return partition * partition
        else:
            return partition * partition * x
        