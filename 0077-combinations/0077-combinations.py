class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def helper(n, path):
            if len(path) == k:
                if path not in res:
                    res.append(path)
                path = path[1:]
            if n == 1:
                return
            for i in range(1, n):
                helper(i, path + [i])
        helper(n, [n])
        return res
        