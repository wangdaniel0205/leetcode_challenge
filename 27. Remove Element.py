class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        l,r = 0, len(nums)-1
        while l <= r:
            if nums[l] == val:
                nums[l], nums[r] = nums[r], nums[l]
                r-=1
            else:
                l+=1
        return r+1


if __name__ == '__main__':
    testCases = [
        [[3,2,2,3], 3]
    ]

    solution = Solution()
    for case in testCases:
        k = solution.removeElement(case[0], case[1])
        print(case[0][:k])
                