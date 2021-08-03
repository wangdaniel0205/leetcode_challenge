class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack(cur, i):
            if i >= len(nums):
                res.append(list(cur))
                return
            
            for k in nums:
                if k not in cur:
                    cur.append(k)
                    backtrack(cur, i+1)
                    cur.pop()
        
        res = []
        backtrack([], 0)
        
        return res