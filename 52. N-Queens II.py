class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """

        def backtrack(placed, y, res):

            # base
            if y == n:
                return res+1
            
            # general
            for x in range(n):
                if x not in placed[0] and y-x not in placed[1] and y+x not in placed[2]:
                    placed[0].add(x)
                    placed[1].add(y-x)
                    placed[2].add(y+x)
                    
                    res = backtrack(placed, y+1, res)
                    
                    placed[0].remove(x)
                    placed[1].remove(y-x)
                    placed[2].remove(y+x)
            
            return res
        
        return backtrack([set(), set(), set()], 0, 0)

if __name__ == '__main__':
    testCases = [
        [2]
    ]

    solution = Solution()
    for case in testCases:
        print(solution.totalNQueens(case[0]))


