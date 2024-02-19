class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        s = bin(n)
        return s.count("1") == 1
        