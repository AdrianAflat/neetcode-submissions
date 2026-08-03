class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        ROWS = len(text1)
        COLS = len(text2)

        dp = []
        for r in range(ROWS + 1):
            temp = []
            for c in range(COLS + 1):
                temp.append(0)
            dp.append(temp)

        #     c  a  t
        #  c [0, 0, 0, 0] 
        #  r [0, 0, 0, 0] 
        #  a [0, 0, 0, 0] 
        #  b [0, 0, 0, 0] 
        #  t [0, 0, 0, 0] 
        #    [0, 0, 0, 0]

        if text1[-1] == text2[-1]:
            dp[ROWS - 1][COLS - 1] = 1

        for i in range(ROWS - 1, -1, -1):
            for j in range(COLS - 1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = dp[i + 1][j + 1] + 1
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])

        return dp[0][0]