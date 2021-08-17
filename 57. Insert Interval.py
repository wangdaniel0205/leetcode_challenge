class Solution(object):
    def insert(self, nums, newInterval):
        """
        :type nums: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        nums.append(newInterval)
        
        nums = sorted(nums, key=lambda num: num[0])
        res = []

        i = j = 0
        num_max = nums[i][1]
        for x in range(0, len(nums)-1):
            if num_max >= nums[x+1][0]: 
                j = x+1
                num_max = max(num_max, nums[j][1])
            else:
                res.append([nums[i][0], num_max])
                i = j = x+1
                num_max = nums[x+1][1]
                
        res.append([nums[i][0], num_max]) 
        return res