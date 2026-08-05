class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix

        ROWS = len(matrix)
        COLS = len(matrix[0])
        for r in range(ROWS):
            curSum = 0
            for c in range(COLS):
                curSum += self.matrix[r][c]
                self.matrix[r][c] = curSum
            curSum = 0

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        startCol = col1
        endCol = col2 
        startRow = row1
        endRow = row2

        result = 0
        for r in range(startRow, endRow + 1):
            if startCol > 0:
                val = self.matrix[r][endCol] - self.matrix[r][startCol - 1]
            else: 
                val = self.matrix[r][endCol]
            result += val
        
        return result


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)