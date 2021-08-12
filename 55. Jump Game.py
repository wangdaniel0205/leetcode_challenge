class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        
        checked = [False for _ in nums]
        checked[0] = True
        for i,k in enumerate(nums):
            if checked[i]:
                for j in range(i+k, i-1, -1):
                    if j >= len(nums)-1: return True
                    if checked[j]: break
                    checked[j] = True
    
    
        return False
        """
        j = len(nums)-1
        for i in range(len(nums)-2, -1, -1):
            if i + nums[i] >= j: j=i
            
        return j == 0
        