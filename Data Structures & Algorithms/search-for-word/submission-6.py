class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        result = [False]
        ROWS = len(board)
        COLS = len(board[0])
        path = set()
        def search(x, y, ptr):
            if ptr == len(word):
                result[0] = True
                return

            if x >= ROWS or x < 0 or y >= COLS or y < 0  or board[x][y] != word[ptr] or (x, y) in path:
                return 

            path.add((x, y))
            search(x + 1, y, ptr + 1)
            search(x - 1, y, ptr + 1)
            search(x, y + 1, ptr + 1)
            search(x, y - 1, ptr + 1)
            path.remove((x, y))

        for r in range(ROWS):
            for c in range(COLS):
                search(r, c, 0)

        return result[0]

        # ["A","B","C","E"]
        # ["S","F","C","S"]
        # ["A","D","E","E"]

