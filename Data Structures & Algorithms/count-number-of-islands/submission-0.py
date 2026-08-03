class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #["1","1","0","0","1"]
        #["1","1","0","0","1"]
        #["0","0","1","0","0"]
        #["0","0","0","1","1"]

        rows = len(grid)
        cols = len(grid[0])
        islands = 0

        def dfs(r, c):
            # out of bounds 
            if r >= rows or r < 0 or c >= cols or c < 0:
                return 
            
            # you reach a 0
            if grid[r][c] == '0':
                return
                
            grid[r][c] = '0'
            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '0':
                    continue 
                else:
                    dfs(r, c)
                    islands += 1

        return islands


        


        