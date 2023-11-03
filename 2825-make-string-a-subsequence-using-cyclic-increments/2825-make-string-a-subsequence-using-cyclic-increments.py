class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        i, j = 0, 0
        n = len(str1)
        m = len(str2)
        while i < n and j < m:
            order = ord(str2[j]) - 97
            while i < n and (ord(str1[i]) - 97 + 1) % 26 != order and  str1[i] != str2[j]:
                i += 1
            if i < n:
                i += 1
                j += 1
        return j == m
        