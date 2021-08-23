class Solution(object):
    def uniquePathsWithObstacles(self, grid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        
        main points: 
            DP -- fix the obstacleGrid, so that 
                2 means both directions are reachable, 
                1 means only one is reachable, 
                0 is neither, 
                -1 is the obstacle
        
            for each grid:
                if the grid is 2 and
                    bottom grid >= 1: add 1 to the res
                    right grid >= 1: add 1 to the res
            
        """

        if grid[0][0] == 1: return 0
        m,n = len(grid), len(grid[0])
        
        
        grid[0][0] = 1
        
        for i in range(1, m):
            grid[i][0] = int(grid[i][0] == 0 and grid[i-1][0] == 1)
        
        for j in range(1, n):
            grid[0][j] = int(grid[0][j] == 0 and grid[0][j-1] == 1)
        
        for i in range(1,m):
            for j in range(1,n):
                if grid[i][j] == 0:
                    grid[i][j] = grid[i-1][j] + grid[i][j-1]
                else:
                    grid[i][j] = 0

        return grid[m-1][n-1]