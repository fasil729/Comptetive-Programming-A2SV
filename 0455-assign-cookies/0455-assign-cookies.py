class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        res, i, ind = 0, 0, 0
        while i < len(g) and ind < len(s):
            if g[i] <= s[ind]:
                res += 1
                i += 1
            ind += 1
        return res
        