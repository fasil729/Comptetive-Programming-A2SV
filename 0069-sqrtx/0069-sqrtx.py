class Solution:
    def mySqrt(self, x: int) -> int:
        low , high = 1, x
        while low <= high:
            mid = low + (high - low) // 2
            square = mid * mid
            if square == x:
                return mid
            elif square < x:
                low = mid + 1
            else:
                high = mid - 1
        return low - 1