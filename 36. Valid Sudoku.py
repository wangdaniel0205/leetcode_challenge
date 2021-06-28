class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
        seen, last_len = set(), 0 
        for i, row in enumerate(board):
            for j, c in enumerate(row):
                if c != '.':
                    seen.add((c,j))
                    seen.add((i,c))
                    seen.add((i/3,j/3,c))
                    if len(seen)-3 != last_len:
                        return False
                    last_len = len(seen)
                    
        return True