class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        direction = [(0, 1), (1, 0), (-1, 0), (0, -1), (-1, 1), (1, -1), (-1, -1), (1, 1)]
        
        if grid[0][0]:
            return - 1
        que = deque([(0, 0, 1)])
        visited = set()
        n = len(grid)
        m = len(grid[0])


        while que:
            row, col, count = que.popleft()
           
            
            
            
            if (row, col) in visited:
                continue
            if (row, col) == (n - 1, m - 1):
                return count
                
            
            visited.add((row, col))
            
            for r, c in direction:
                nr = row + r
                nc = col + c
                
                if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == 0:
                    que.append((nr, nc, count + 1))
        return -1
                    
                
            
            

            

        