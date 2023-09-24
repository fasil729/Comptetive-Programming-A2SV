class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        def inbound(row, col):
            return 0 <= col <= row
        @cache
        def dp(row, col):
            if not inbound(row, col):
                return 0
            if row == col == 0:
                return poured
            left = max(dp(row - 1, col - 1) - 1, 0) / 2
            right = max(dp(row - 1, col) - 1, 0) / 2
            return  left + right
        return min(dp(query_row, query_glass), 1.0)
            
