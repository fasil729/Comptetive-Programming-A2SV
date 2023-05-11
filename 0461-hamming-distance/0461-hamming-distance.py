class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        num = x ^ y
        k  = 31
        res = 0
        while k >= 0:
            if num & 1 << k:
                res += 1
            k -= 1
        return res