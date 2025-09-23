class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            seen = set()
            for j in range(9):
                num = board[i][j]
                if num == ".": continue
                if num in seen: return False
                seen.add(num)

        for i in range(9):
            seen = set()
            for j in range(9):
                num = board[j][i]
                if num == ".": continue
                if num in seen: return False
                seen.add(num)

        for square in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (square//3) * 3 + i
                    col = (square%3) * 3 + j
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])
        
        return True