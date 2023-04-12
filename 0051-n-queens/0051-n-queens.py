class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        arr = []
        result = []
        def helper(row, placed):
            if row == n:
                result.append(arr.copy())
                return
            
            for col in range(0, n):
                breaked = False
                for colum, rown in placed:
                        if colum == col or abs(rown - row) == abs(colum - col):
                            breaked = True
                            break
                if not breaked:
                    placed.append((col, row))
                    string = "." * (col) + "Q" + "." * (n - col - 1)
                    arr.append(string)
                    helper(row + 1, placed)
                    placed.pop()
                    arr.pop()
            
        helper(0, [])
        return result
        
        
        
        
        
        
        
        