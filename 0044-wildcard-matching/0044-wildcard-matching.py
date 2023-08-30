class Solution:

    def isMatch(self, s: str, p: str) -> bool:
        memo = {}

        def recur(i, j):
            if (i, j) in memo:
                return memo[(i, j)]

            if i >= len(s) and j >= len(p):
                memo[(i, j)] = True
            elif j >= len(p):
                memo[(i, j)] = False
            elif i >= len(s):
                if p[j] == '*':
                    memo[(i, j)] = recur(i, j + 1)
                else:
                    memo[(i, j)] = False
            elif p[j] == '*':
                memo[(i, j)] = recur(i + 1, j + 1) or recur(i, j + 1) or recur(i + 1, j)
            elif p[j] == '?' or p[j] == s[i]:
                memo[(i, j)] = recur(i + 1, j + 1)
            else:
                memo[(i, j)] = False

            return memo[(i, j)]

        return recur(0, 0)
        