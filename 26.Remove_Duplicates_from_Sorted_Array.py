class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return len(nums)
        
        l, r = 0, 1
        while r < len(nums):
            if nums[l] != nums[r]:
                l = r
                r += 1
            elif nums[l] == nums[r]:
                nums.pop(r)
            
        return len(nums)