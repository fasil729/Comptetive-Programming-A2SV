class Solution:
    def totalNQueens(self, n: int) -> int:
        board = [['' for i in range(n)] for j in range(n)]
        self.queens = n
        # self.placed = 0
        self.ans = 0
        # self.queen_pos = []
        self.place(0,board)
        return self.ans
    
    def place(self,i,board,queens=None,placed=0):
        if placed == self.queens:
            self.ans += 1
            return
        if i>= self.queens:
            return
        if not queens:
            queens = []
        for j in range(self.queens):
            if not self.intersect(queens+[[i,j]],placed,board):
                board[i][j] = 'Q'
                self.place(i+1,board,queens+[[i,j]],placed+1)
                board[i][j] = ''
    
    def intersect(self,queens,placed,board):
        if placed < 1:
            return False
        for queen in queens:
            q_x,q_y = queen[0],queen[1]
            for i in range(self.queens):
                if board[i][q_y] == 'Q' and i!=q_x:
                    return True
                if board[q_x][i] == 'Q' and i!=q_y:
                    return True
                
            # right down diagonal check
            while q_x+1<self.queens and q_y+1<self.queens:
                q_x,q_y = q_x+1,q_y+1
                if board[q_x][q_y] == 'Q':
                    return True
                
            # left down diagonal check
            q_x,q_y = queen[0],queen[1]
            while q_x-1>=0 and q_y+1<self.queens:
                q_x,q_y = q_x-1,q_y+1
                if board[q_x][q_y] == 'Q':
                    return True
                
            # right up diagonal check
            q_x,q_y = queen[0],queen[1]
            while q_x+1<self.queens and q_y-1>=0:
                q_x,q_y = q_x+1,q_y-1
                if board[q_x][q_y] == 'Q':
                    return True
                
            # left up diagonal check
            q_x,q_y = queen[0],queen[1]
            while q_x-1>=0 and q_y-1>=0:
                q_x,q_y = q_x-1,q_y-1
                if board[q_x][q_y] == 'Q':
                    return True
        return False
        