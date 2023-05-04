class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        
        
        def helper(n):
            if n == 1:
                return "0"
            sn = helper(n - 1)
            inv = ["0" if i == "1" else "1" for i in sn]
            rev = "".join(reversed(inv))
            return sn + "1" + rev
        return helper(n)[k - 1]