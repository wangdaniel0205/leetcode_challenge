from numpy import inf
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        
        if len(nums) < 2:
            return
        
        for i in range(len(nums)-2, -1 ,-1):
            if nums[i] < nums[i+1]:
                diff, nxt = nums[i+1] - nums[i], i+1
                for j in range(i+2, len(nums)):
                    cur = nums[j] - nums[i]
                    if cur > 0 and cur <= diff:
                        diff, nxt = cur, j
                nums[i], nums[nxt] = nums[nxt], nums[i]
                nums[i+1:] = nums[i+1:][::-1]
                return
        
        
       
        nums.sort()
        return