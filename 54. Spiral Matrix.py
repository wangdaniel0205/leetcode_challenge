class Solution(object):
    def spiralOrder(self, mat):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        x_len,y_len = len(mat[0])+1, len(mat)
        layer=0
        res = []
        x, y = -1, 0
        
        while True:
            x_len -= 1
            if x_len == 0: return res
            for _ in range(x_len):
                x+=1
                res.append(mat[y][x]) 

            y_len -= 1
            if y_len == 0: return res
            for _ in range(y_len):
                y+=1
                res.append(mat[y][x])

            x_len -= 1
            if x_len == 0: return res
            for _ in range(x_len):
                x-=1
                res.append(mat[y][x]) 

            y_len -= 1
            if y_len == 0: return res
            for _ in range(y_len):
                y-=1
                res.append(mat[y][x])
