class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        def get_next_empty_pos(prev=[0,0]):
            nxt = [prev[0], prev[1]]
            while nxt[0] < 9 and board[nxt[0]][nxt[1]] != '.':
                nxt[1] += 1
                if nxt[1] == 9: nxt = [nxt[0]+1, 0]
            return nxt
        
        def add_to_board(pos, c, seen): 
            # add to board if valid and return True
            # if not valid, return False 
            
            safe = not any(((pos[0], c) in seen, (c, pos[1]) in seen, (pos[0]//3, pos[1]//3, c) in seen))
            
            if safe:
                # add to board
                board[pos[0]][pos[1]] = c
                
                # update seen
                seen.add((pos[0], c))
                seen.add((c, pos[1]))
                seen.add((pos[0]//3, pos[1]//3, c))
            
            return safe
            
            
        def fill(pos, seen):
            
            # base: nothing else to fill
            if pos[0] == 9:
                return True
            
            # general
            for c in ['1','2','3','4','5','6','7','8','9']:
                if add_to_board(pos, c, seen):
                    # c added to board
                    
                    if fill(get_next_empty_pos(pos), seen): 
                        return True
                    
                    # undo board and seen
                    board[pos[0]][pos[1]]  = '.'
                    seen.remove((pos[0], c))
                    seen.remove((c, pos[1]))
                    seen.remove((pos[0]//3, pos[1]//3, c))
                    
            # all combination tried: not fillable
            return False
        
        
        # make the seen 
        seen = set()
        for i, row in enumerate(board):
            for j, c in enumerate(row):
                if c != '.':
                    seen.add((i,c))
                    seen.add((c,j))
                    seen.add((i//3, j//3, c))


        fill(get_next_empty_pos(), seen)
        

if __name__ == '__main__':
    testCases = [
        [[["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]]
    ]

    solution = Solution()
    for case in testCases:
        solution.solveSudoku(case[0])
        print(case[0])