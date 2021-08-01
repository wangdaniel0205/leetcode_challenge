class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = i = 0
        while i+1 < len(nums):
            if i+nums[i]+1 >= len(nums):
                return res+1
            score, index = 0, i
            for j in range(1, nums[i]+1):
                if nums[i+j]+j > score:
                    score = nums[i+j]+j
                    index = i+j
            i = index
            res += 1
        return res

if __name__ == '__main__':
    testCases = [
        [[2,3,1]]
    ]

    solution = Solution()
    for case in testCases:
        print(solution.jump(case[0]))