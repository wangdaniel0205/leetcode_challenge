class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def search(lo, hi):
            if hi < lo:
                return -1
        
            mid = (lo+hi) // 2
            if (mid-1 < 0 or nums[mid-1] < target) and target <= nums[mid]: # perfect position
                return mid
            elif nums[mid] < target:
                return search(mid+1, hi)
            else:
                return search(lo, mid-1)
        
        res = search(0, len(nums)-1)
        return len(nums) if res == -1 else res