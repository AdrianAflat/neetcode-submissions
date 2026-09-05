class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        seen = set()
        freshFruit = [0]
        q = deque()

        # counting fresh fruit and finding starting postition for BFS(rotten fruit)
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    freshFruit[0] += 1
                if grid[r][c] == 2:
                    q.append((r, c))
                    seen.add((r, c))

        if freshFruit[0] == 0:
            return 0

        # if a (r, c) it gets added to the queue
        def addFruit(r, c):
            if (r < 0 or r >= ROWS or c < 0 or c >= COLS or
                (r, c) in seen or grid[r][c] == 0 or grid[r][c] == 2):
                return 

            seen.add((r ,c))
            grid[r][c] = 2
            freshFruit[0] -= 1
            q.append((r, c))


        timePassed = -1
        while q:
            timePassed += 1
            for i in range(len(q)):
                r, c = q.popleft()

                addFruit(r + 1, c)
                addFruit(r - 1, c)
                addFruit(r, c + 1)
                addFruit(r, c - 1)

        if freshFruit[0] == 0:
            return timePassed
        else: 
            return -1
                
