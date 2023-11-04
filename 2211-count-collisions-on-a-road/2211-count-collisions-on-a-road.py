class Solution:
    def countCollisions(self, directions: str) -> int:
        stop = False
        ans = 0
        r = 0    
        for d in directions:   
            if d == "R":
                r += 1
                stop = True
            elif d == "S":
                ans += r
                r = 0
                stop = True
            elif d == "L" and stop:
                ans += r + 1
                r = 0
        return ans