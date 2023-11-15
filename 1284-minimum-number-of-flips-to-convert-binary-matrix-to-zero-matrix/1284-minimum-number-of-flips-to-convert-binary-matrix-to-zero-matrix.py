class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
        
        n = len(mat)
        m = len(mat[0])
        
        def inbound(row, col):
            return 0 <= col < m and 0 <= row < n
        
        def swap(mat, row, col):
            
            direc = [[-1, 0], [0, -1], [0, 1], [1, 0]]
            matrix = [arr.copy() for arr in mat]
            matrix[row][col] = 1 - matrix[row][col]
            for r, c in direc:
                n_r = row + r
                n_c = col + c
                if inbound(n_r, n_c):
                    matrix[n_r][n_c] = 1 - matrix[n_r][n_c]
                
                
            return matrix
        
        
            
        queue = [mat]
       
        zero = [[0] * m for _ in range(n)]
        oper = 0
        visited = set() 
        
        while queue:
            new_queue = []
            
            for matr in queue:
                
                if matr == zero:
                    return oper
                if str(matr) not in visited:
                    
                    visited.add(str(matr))
                    for r in range(n):
                        for c in range(m):
                            new_matr = swap(matr, r, c)
                            new_queue.append(new_matr)
                    
            oper += 1
            queue = new_queue
        
        return -1
                    
                
        

        
        