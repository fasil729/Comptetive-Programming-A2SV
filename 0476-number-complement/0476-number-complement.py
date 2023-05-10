class Solution:
    def findComplement(self, num):
        mask, tmp = 0, num
        while tmp:
            mask = (mask << 1) | 1
            tmp >>= 1
        return mask ^ num