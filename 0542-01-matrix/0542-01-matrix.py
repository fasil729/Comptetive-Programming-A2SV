class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        direc = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        m = len(mat)
        n = len(mat[0])
        
        # print(ans)
        def bfs():
            ans = []
            for _ in range(m):
                arr = [0] * n
                ans.append(arr)
            visited = set([(row, col) for row in range(m) for col in range(n) if not mat[row][col]])
            queue = deque([(row, col) for row in range(m) for col in range(n) if not mat[row][col]])
            count = 0
            while queue:
                
                
               
                for i in range(len(queue)):
                   
                    row, col = queue.popleft()
                    ans[row][col] = count
                    

                    for r, c in direc:
                        nr = row + r
                        nc = col + c

                        if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visited and mat[nr][nc]:
                            visited.add((nr, nc))
                            queue.append((nr, nc))
                count += 1
            return ans
                        
        
        return bfs()
        
            
        