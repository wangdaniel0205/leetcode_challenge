class Solution(object):
    def rotate(self, mat):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        
        n = len(mat)
        
        # transpose
        for y in range(n):
            for x in range(n):
                if y == x: continue
                elif y<x:
                    mat[y][x], mat[x][y] = mat[x][y], mat[y][x]
                
                    
        # reverse vertically
        for row in mat:
            i, j = 0, n-1
            while i < j:
                row[i], row[j] = row[j], row[i]
                i, j = i+1, j-1

                
        
    