class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        rotten = [(row, col) for row in range(m) for col in range(n) if grid[row][col] == 2 ]
        fresh = len([row for row in range(m) for col in range(n) if grid[row][col] == 1])
        visited = set(rotten)
        direc = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        queue = deque([(row, col, 0) for row, col in rotten])
        f = 0
        count = 0
        while queue:
            for i in range(len(queue)): 
                row, col, count = queue.popleft()
                for r, c in direc:
                    nr = row + r
                    nc = col + c
                    if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visited:
                        visited.add((nr, nc))
                        if grid[nr][nc] == 1:
                            grid[nr][nc] = 2
                            
                            queue.append((nr, nc, count + 1))
                            f += 1
            
                        
       
        if fresh == f:
            return count
        else:
            return -1
                    