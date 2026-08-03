class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ROWS = m
        COLS = n
        dp = []
        for r in range(ROWS + 1):
            row = []
            for c in range(COLS + 1):
                row.append(0)
            dp.append(row)

        dp[ROWS - 1][COLS - 1] = 1
        
        for r in range(ROWS - 1, -1, -1):
            for c in range(COLS - 1, -1, -1):
                dp[r][c] += dp[r + 1][c]
                dp[r][c] += dp[r][c + 1]

        return dp[0][0]