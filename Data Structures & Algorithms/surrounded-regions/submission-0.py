class Solution:
    def solve(self, board: List[List[str]]) -> None:

        #["X","X","X","X"]
        #["X","O","O","X"]
        #["X","X","O","X"]
        #["X","O","X","X"]

        #["X","X","X","X"],
        #["X","O","O","X"],
        #["X","X","O","X"],
        #["X","O","X","X"]

        safe = set() # stores the tiles that won't be turned to 'X'
        seen = set() # stores checked tiles
        ROWS, COLS = len(board), len(board[0])

        def dfs(r, c):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or (r, c) in seen:
                return 

            seen.add((r, c))

            if board[r][c] == 'X':
                return
            elif board[r][c] == 'O':
                safe.add((r, c))

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(ROWS):
            dfs(r, 0)
            dfs(r, COLS - 1)

        for c in range(COLS):
            dfs(0, c)
            dfs(ROWS - 1, c)
                
        for r in range(ROWS):
            for c in range(COLS):
                if ((r, c)) not in safe:
                    board[r][c] = 'X' 
    