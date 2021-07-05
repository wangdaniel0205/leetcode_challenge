class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()

        def combination(cur):
            for k in candidates:
                if len(cur) > 0 and k < cur[-1]:
                    continue 
                elif sum(cur) + k <= target:
                    cur.append(k)
                    
                    if sum(cur) == target:
                        res.append(list(cur))
                    else:
                        combination(cur)
                    
                    cur.pop()
                else:
                    break
            
        
        res, cur = [], []  
        combination(cur)
        
        return res


if __name__ == '__main__':
    testCases = [
        [[2,3,5], 8]
    ]

    solution = Solution()
    for case in testCases:
        print(solution.combinationSum(case[0], case[1]))