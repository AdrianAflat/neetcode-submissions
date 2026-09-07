class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS = len(board)
        COLS = len(board[0])
        safe = set() # stores safe (r, c) pairs

        def markSafe(r, c):
            if  r < 0 or c < 0 or r >= ROWS or c >= COLS or board[r][c] == "X" or (r, c) in safe:
                return 
            
            safe.add((r, c))

            markSafe(r + 1, c)
            markSafe(r - 1, c)
            markSafe(r, c + 1)
            markSafe(r, c - 1)

        for r in range(ROWS):
            if board[r][0] == "O":
                markSafe(r, 0)
            if board[r][COLS - 1] == "O":
                markSafe(r, COLS - 1)

        for c in range(COLS):
            if board[0][c] == "O":
                markSafe(0, c)
            if board[ROWS - 1][c] == "O":
                markSafe(ROWS - 1, c)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O" and (r, c) not in safe:
                    board[r][c] = "X"
