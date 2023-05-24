class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        direction = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        
        
        que = deque()
        visited = set()
        visited.add((entrance[0], entrance[1]))
        n = len(maze)
        m = len(maze[0])
        row, col, count = entrance[0], entrance[1], 0
        for r, c in direction:
                nr = row + r
                nc = col + c
                
                if 0 <= nr < n and 0 <= nc < m and maze[nr][nc] == ".":
                    que.append((nr, nc, count + 1))

        while que:
            row, col, count = que.popleft()
            
           
            if (row, col) in visited:
                continue
           
                
            
            visited.add((row, col))
            
            for r, c in direction:
                nr = row + r
                nc = col + c
                
                if not (0 <= nr < n and 0 <= nc < m):
                    return count
                
                if maze[nr][nc] == ".":
                    que.append((nr, nc, count + 1))
        return -1