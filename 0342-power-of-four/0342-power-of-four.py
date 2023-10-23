class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n < 0:
            return False
        binNum = bin(n)[2:]
        leng = len(binNum)
        if leng % 2 == 1 and binNum.count("1") == 1:
            return True
        
        return False
        