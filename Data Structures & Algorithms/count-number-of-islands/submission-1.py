class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        seen = set() # stores (x, y) tuples 
        def dfs(x, y):
            if x < 0 or y < 0 or x >= ROWS or y >= COLS or (x, y) in seen or grid[x][y] == "0":
                return 

            seen.add((x, y))
            dfs(x - 1, y)
            dfs(x + 1, y)
            dfs(x, y + 1)
            dfs(x, y - 1)


        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in seen:
                    res += 1
                    dfs(r, c)

        return res