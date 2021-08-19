class Solution:
    def generateMatrix(self, n):
        ans = [[0 for _ in range(n)] for _ in range(n)]
        
        dt = 'r'
        i, j = 0, 0
        for k in range(n**2):
            ans[i][j] = k+1
            if dt == 'r':
                j += 1
                if j >=n or ans[i][j] != 0:
                    j -= 1
                    dt = 'd'
                    i += 1
            elif dt == 'd':
                i += 1
                if i >=n or ans[i][j] != 0:
                    i -= 1
                    dt = 'l'
                    j -= 1
            
            elif dt == 'l':
                j -= 1
                if j <= -1 or ans[i][j] != 0 :
                    j += 1
                    dt = 'u'
                    i -= 1
            elif dt == 'u':
                i -= 1
                if i <= -1 or ans[i][j] != 0:
                    i += 1
                    dt = 'r'
                    j += 1
        return ans 