
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = 9

        for row in board:
            seen = set()
            for value in row:
                if value != ".":
                    if value in seen:
                        return False
                    seen.add(value)

        for col in range(n):
            seen = set()
            for row in range(n):
                value = board[row][col]
                if value != ".":
                    if value in seen:
                        return False
                    seen.add(value)

        for block_row in range(0, n, 3):
            for block_col in range(0, n, 3):
                seen = set()
                for i in range(3):
                    for j in range(3):
                        value = board[block_row + i][block_col + j]
                        if value != ".":
                            if value in seen:
                                return False
                            seen.add(value)

        return True
