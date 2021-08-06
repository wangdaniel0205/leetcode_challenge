class Solution(object):
    def permuteUnique(self, nums):
        ans = [[]]
        for n in nums:
            new_ans = []
            for l in ans:
                for i in range(len(l)+1):
                    new_ans.append(l[:i]+[n]+l[i:])
                    if i<len(l) and l[i]==n: break              #handles duplication
            ans = new_ans
        return ans

if __name__ == '__main__':
    testCases = [
        [[1,3,1]]
    ]

    solution = Solution()
    for case in testCases:
        print(solution.permuteUnique(case[0]))