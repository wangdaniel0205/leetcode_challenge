class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def binarySearch(l,r,target):
            if r < l:
                return -1
            
            m = (l+r)//2
            if nums[m] == target:
                return m
            elif target < nums[m]:
                return binarySearch(l,m-1,target)
            else:
                return binarySearch(m+1,r,target)
        
        def brokenSearch(l,r,target):
            if r < l:
                return -1
            
            m = (l+r)//2
            if nums[m] == target:
                return m
            
            # find the broken side: the greater absolute difference between the side and mid
            
            elif abs(nums[m] - nums[l]) > abs(nums[m] - nums[r]): # the broken side is left
                if nums[m] < target and target <= nums[r]: # if target is in sorted range
                    return binarySearch(m+1,r,target)
                else:
                    return brokenSearch(l,m-1,target)
            
            else: # the broken side is right
                if nums[l] <= target and target < nums[m]: # if target is in sorted range
                    return binarySearch(l,m-1,target)
                else:
                    return brokenSearch(m+1,r,target) 
            
        return brokenSearch(0,len(nums)-1,target)

if __name__ == '__main__':
    testCases = [
        [[4,5,6,7,0,1,2], 0]
    ]

    solution = Solution()
    for case in testCases:
        print(solution.search(case[0], case[1]))