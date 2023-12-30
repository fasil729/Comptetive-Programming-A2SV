class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        n = len(matrix)
        m = len(matrix[0])
        
        transpose = [
            [matrix[row][col] for row in range(n)] 
            for col in range(m)
        ]
        
        return transpose