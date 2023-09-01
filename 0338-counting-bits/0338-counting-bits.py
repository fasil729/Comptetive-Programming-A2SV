class Solution:
    def countBits(self, n: int) -> List[int]:
        # bruteforce approach
        res = []
        for i in range(n + 1):
            res.append(bin(i).count("1"))
        return res        