class Solution:
    def reverse(self, x: int) -> int:
        if x not in range(-9,9):
            x = int(str(x)[::-1].lstrip('0')) if x >= 0 else int(f"-{str(x)[:0:-1]}".lstrip('0'))
        return x if (x < 2**31-1 and x > -2**31) else 0