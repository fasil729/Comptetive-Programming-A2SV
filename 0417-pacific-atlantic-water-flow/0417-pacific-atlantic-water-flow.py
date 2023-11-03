class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
       
        n = len(heights)
        m = len(heights[0])
        
        def inbound(row, col):
            return 0 <= row < n and 0 <= col < m
        def bfs(queue):
            
            queue = deque(queue)
            visited = set(queue)
            
            while queue:
                row, col = queue.popleft()
                direc = [[-1, 0], [1, 0], [0, 1], [0, -1]]
                h = heights[row][col]
                for r, c in direc:
                    n_r = row + r
                    n_c = col + c
                
                    if inbound(n_r, n_c) and (n_r, n_c) not in visited and heights[n_r][n_c] >= h:
                        queue.append((n_r, n_c))
                        visited.add((n_r, n_c))
            return visited
        
        pacfic_bound = [(0, col) for col in range(m)] + [(row, 0) for row in range(n)]
        atlantic_bound = [(n - 1, col) for col in range(m)] + [(row, m - 1) for row in range(n)]
        pacific = bfs(pacfic_bound)
        atlantic = bfs(atlantic_bound)
        
        return list(pacific & atlantic)
                    
                    
        