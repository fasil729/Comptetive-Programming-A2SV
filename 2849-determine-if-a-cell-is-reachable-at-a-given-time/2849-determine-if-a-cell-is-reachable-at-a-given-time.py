class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        if t == 1 and (sx, sy) == (fx, fy):
            return False
        return t >= max(abs(sx - fx), abs(sy - fy))
        