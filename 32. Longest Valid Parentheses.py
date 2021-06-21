class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        table = [False for i in s]
        res = left = cur = 0
        
        # init table
        for i,c in enumerate(s):
            if c == '(':
                left += 1
            else:
                if left > 0:
                    j = i-1
                    while table[j]: j -=1 
                    table[i] = table[j] = True 
                    left -= 1
                    
        # table look up
        for val in table:
            if val:
                cur += 1
            else:
                res = max(res, cur)
                cur = 0
        res = max(res, cur)
        return res