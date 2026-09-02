class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        # 1. find start of island 
        startX = 0
        startY = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    startX = r
                    startY = c
                    break

        # 2. dfs and add one whenever you leave the island
        res = [0]
        visit = set()
        def dfs(x, y):
            if x < 0 or x >= ROWS or y < 0 or y >= COLS or grid[x][y] == 0:
                res[0] += 1
                return

            if (x, y) in visit:
                return 

            visit.add((x, y))

            dfs(x + 1, y)
            dfs(x - 1, y)
            dfs(x, y + 1)
            dfs(x, y - 1)

        dfs(startX, startY)
        return res[0]