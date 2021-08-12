class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = cur_max = 0
        
        for num in nums:
            cur_max += num
            
            if cur_max > res: res = cur_max
            if cur_max < 0:
                cur_max = 0
                continue
            
                        
        return res if res > 0 else max(nums)