class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        @cache
        def dp(i, j):
            if i == j:
                return 0
            res = float("inf")
            for k in range(i, j):
                res = min(res, max(arr[i:k + 1]) * max(arr[k + 1:j + 1]) + dp(i, k) + dp(k + 1, j))
            
            return res
        return dp(0, len(arr) - 1)
                