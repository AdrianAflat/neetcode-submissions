class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dp = {}
        ROWS = len(matrix)
        COLS = len(matrix[0])

        def dfs(x, y, prevVal):
            if x >= ROWS or y >= COLS or x < 0 or y < 0 or matrix[x][y] <= prevVal:
                return 0

            if (x, y) in dp:
                return dp[(x, y)]
            
            res = 1
            res = max(res, 1 + dfs(x + 1, y, matrix[x][y]))
            res = max(res, 1 + dfs(x - 1, y, matrix[x][y]))
            res = max(res, 1 + dfs(x, y + 1, matrix[x][y]))
            res = max(res, 1 + dfs(x, y - 1, matrix[x][y]))
            
            dp[(x, y)] = res
            

            return dp[(x, y)]


        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, -1)

        return max(dp.values())