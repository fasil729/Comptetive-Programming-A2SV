class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        row, col = click
        visited = set()
        n = len(board)
        m = len(board[0])

        if board[row][col] == "M":
            board[row][col] = "X"
            return board
        
        def dfs(row, col):
            visited.add((row, col))
            if board[row][col] == "M":
                return

            direc = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1)]
            adj_mines = 0
            
            # count adjacent mines
            for r, c in direc:
                n_r = row + r
                n_c = col + c
                if  0 <= n_r < n and 0 <= n_c < m and board[n_r][n_c] == "M":
                    adj_mines += 1
            # check if there are adjacent mines
            if adj_mines:
                board[row][col] = str(adj_mines)
                return
            
            # if there is not adjacent mines continue recursion
            board[row][col] = "B"
            
            for r, c in direc:
                n_r = row + r
                n_c = col + c
                if  0 <= n_r < n and 0 <= n_c < m and not (n_r, n_c) in visited:
                     dfs(n_r, n_c)

        dfs(row, col)
        return board
                    
                