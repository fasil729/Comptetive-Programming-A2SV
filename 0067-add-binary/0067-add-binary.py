class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = ""
        rem = 0
        i, j = len(a) - 1, len(b) - 1
        while i >=0 and j >= 0:
            s = int(a[i]) + int(b[j]) + rem
            rem = s // 2
            res += str(s % 2)
            i -= 1
            j -= 1
        while i >=0:
            s = int(a[i]) + rem
            rem = s // 2
            res += str(s % 2)
            i -= 1

        while j >= 0:
            s = int(b[j]) + rem
            rem = s // 2
            res += str(s % 2)
            j -= 1
        if rem:
            res += str(rem)
        return res[::-1]
            