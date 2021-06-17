class Solution(object):
    '''
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l = len(nums)
        
        for i in range(l):
            for j in range(l):
                if i == j:
                    continue
                if nums[i] + nums[j] == target:
                    return [i,j]
    '''
    # not brute force
    def twoSum(self, nums, target):
        hashMap = {}
        for i, k in enumerate(nums):
            complement = target - k
            if complement in hashMap:
                return [hashMap[complement], i]
            else:
                hashMap[k] = i 