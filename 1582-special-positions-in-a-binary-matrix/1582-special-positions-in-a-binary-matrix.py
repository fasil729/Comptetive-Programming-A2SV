class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        
        n = len(mat)
        m = len(mat[0])
        col_sum = []
        row_sum = []
        
        for row in range(n):
            row_sum.append(sum([mat[row][col] for col in range(m)]))
            
        for col in range(m):
            col_sum.append(sum([mat[row][col] for row in range(n)]))
        
        ans = 0
        for row in range(n):
            for col in range(m):
                if mat[row][col] == row_sum[row] == col_sum[col] == 1:
                    ans += 1
                    
        return ans
        