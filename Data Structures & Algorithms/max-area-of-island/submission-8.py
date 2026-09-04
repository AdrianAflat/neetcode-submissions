class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        res = 0
        seen = set() # (x, y) pairs alr visited 

        def dfs(x, y):
            if x < 0 or y < 0 or x >= ROWS or y >= COLS or grid[x][y] == 0 or (x, y) in seen:
                return 0

            seen.add((x, y))

            return (1 + dfs(x + 1, y) + dfs(x - 1, y) + dfs(x, y + 1) + dfs(x, y - 1))



        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    res = max(res, dfs(r, c))

        return res

        # [0 0 1 0 0 0 0 1 0 0 0 0 0]
        # [0,0,0,0,0,0,0,1,1,1,0,0,0]
        # [0,1,1,0,1,0,0,0,0,0,0,0,0]
        # [0,1,0,0,1,1,0,0,1,0,1,0,0]
        # [0,1,0,0,1,1,0,0,1,1,1,0,0]
        # [0,0,0,0,0,0,0,0,0,0,1,0,0]
        # [0,0,0,0,0,0,0,1,1,1,0,0,0]
        # [0,0,0,0,0,0,0,1,1,0,0,0,0]