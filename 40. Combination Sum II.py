from collections import Counter
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        
        # add occurance of unique candidates into a dictionary
        count = Counter(candidates)
        vals = list(count.keys())
                
        
        # run recursive similar to Combination Sum I
        res = []
        def backtrack(comb, remain, cur):
            
            # base
            if remain <= 0:
                if remain == 0:
                    res.append(list(comb))
                return
                
            # general
            for i in range(cur, len(vals)):
                val = vals[i]
                
                if count[val] <= 0: 
                    continue
                    
                comb.append(val)
                count[val] -= 1
                
                backtrack(comb, remain-val, i)
                
                comb.pop()
                count[val] += 1
                

        
        backtrack([], target, 0)
        return res
if __name__ == '__main__':
    testCases = [
        [[10,1,2,7,6,1,5],8]
    ]

    solution = Solution()
    for case in testCases:
        print(solution.combinationSum2(case[0], case[1]))