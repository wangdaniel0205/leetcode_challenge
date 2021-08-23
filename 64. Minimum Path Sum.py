class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        res = grid[0][0]
        
        
        i_max = len(grid)-1
        j_max = len(grid[0])-1

        if i_max == j_max and i_max == 0:
            return res
        elif i_max == 0:
            return sum(grid[0])
        
        
        i_start, j_start = 1,0
        
        while j_start < j_max:
            
            i, j = i_start, j_start
            
            while j <= j_max and i <= i_max and i >= 0: # not out of index
                if i == 0:
                    grid[i][j] = grid[i][j] + grid[i][j-1]
                elif j == 0:
                    grid[i][j] = grid[i][j] + grid[i-1][j]
                else:
                    grid[i][j] = grid[i][j] + min((grid[i-1][j], grid[i][j-1]))
            
                i -= 1
                j += 1 
            
            
            # the adjustment for next loop
            if i_start < i_max:
                i_start += 1
            else:
                j_start += 1 
        

            
            
        return grid[i_max][j_max] + min((grid[i_max-1][j_max], grid[i_max][j_max-1]))
        
