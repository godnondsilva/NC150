class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [0]*9
        cols = [0]*9
        squares = [0]*9

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".": continue
                
                val = int(board[r][c]) - 1
                shifted_val = 1 << val
                if shifted_val & rows[r]:
                    return False
                if shifted_val & cols[c]:
                    return False
                if shifted_val & squares[(r//3) * 3 + (c//3)]:
                    return False

                cols[c] |= shifted_val
                rows[r] |= shifted_val
                squares[((r//3) * 3 + (c//3))] |= shifted_val
        return True