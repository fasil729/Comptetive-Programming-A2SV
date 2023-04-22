class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row_count = defaultdict(set)
        col_count = defaultdict(set)
        box_count = defaultdict(set)
        for row in range(9):      # count non-empety cells row, col, and box
            for col in range(9):
                val = board[row][col]
                if val != ".":
                    box = 3 * (row // 3) + (col // 3)
                    row_count[row].add(val)
                    col_count[col].add(val)
                    box_count[box].add(val)
        def backtrack(row, col):
            if row == 9:
                return True
            val = board[row][col]
            box = 3 * (row // 3) + (col // 3)
            new_col = (col + 1) % 9
            new_row = row + ((col + 1) // 9)
            if val != ".":
                return backtrack(new_row, new_col)
               
            
            for num in range(1, 10):
                num = str(num)
                if num in row_count[row] or num in col_count[col] or num in box_count[box]:
                    continue
                row_count[row].add(num)
                col_count[col].add(num)
                box_count[box].add(num)
                board[row][col] = num
                if backtrack(new_row, new_col):
                    return True
                row_count[row].remove(num)
                col_count[col].remove(num)
                box_count[box].remove(num)
                board[row][col] = "."
            return False
        backtrack(0, 0)
        