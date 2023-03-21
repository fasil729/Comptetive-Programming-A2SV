class NumMatrix:
    """
    prefix[i][j]=​prefix[i−1][j]+prefix[i][j−1] − prefix[i−1][j−1]+arr[i][j]​
    """

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        
        row = len(matrix)
        col = len(matrix[0])
        self.prefix = [[0] * (col + 1)]
        for r in range(row):    
            column = [0]
            for c in range(col):
                column.append(self.prefix[r][c+1] + column[c] - self.prefix[r][c] + matrix[r][c]) 
            self.prefix.append(column)
        print(self.prefix)

            

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.prefix[row2 + 1][col2 + 1] - self.prefix[row1][col2 + 1] - self.prefix[row2 + 1][col1] + self.prefix[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)