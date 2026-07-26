class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        results = []
        used_cols = set()
        used_desc_diagonals = set()
        used_asc_diagonals = set()

        board = [["."]*n for _ in range(n)]

        def backtrack(row:int) -> None:
            if row == n:
                results.append(["".join(board_row) for board_row in board])
                return

            for col in range(n):
                desc_diagonal = row-col
                asc_diagonal = row+col

                if (
                    col in used_cols
                    or desc_diagonal in used_desc_diagonals
                    or asc_diagonal in used_asc_diagonals):
                    continue

                board[row][col] = "Q"
                used_cols.add(col)
                used_desc_diagonals.add(desc_diagonal)
                used_asc_diagonals.add(asc_diagonal)

                backtrack(row + 1)

                board[row][col] = "."
                used_cols.remove(col)
                used_desc_diagonals.remove(desc_diagonal)
                used_asc_diagonals.remove(asc_diagonal)



        backtrack(0)
        return results
                