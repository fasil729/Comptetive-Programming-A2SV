class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m = len(img[0])
        n = len(img)
        
        def inbound(row, col):
            return 0 <= row < n and 0 <= col < m
        
        neighbours = [[0, 1], [0, -1], [1, 1], [-1, 1], [-1, -1], [1, -1], [1, 0], [-1, 0]]
        ans = [[0] * m for _ in range(n)]
        
        for row in range(n):
            for col in range(m):
                tot = img[row][col]
                count = 1
                
                for r, c in neighbours:
                    n_r = row + r
                    n_c = col + c
                    
                    if inbound(n_r, n_c):
                        tot += img[n_r][n_c]
                        count += 1
                ans[row][col] = tot // count
        
        return ans
                