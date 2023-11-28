class Solution:
    def numberOfWays(self, corridor: str) -> int:
        
        # handle when there is no possible ways
        if corridor.count("S") == 0 or corridor.count("S") % 2 != 0:
            return 0
        
        MOD = 10 ** 9 + 7
        
        ans = 1
        count = 0
        possible = 0
        for letter in corridor:
            if letter == "S" and count == 2:
                count = 0
                ans *= possible
                possible = 0
            if letter == "S":
                count += 1
            if count == 2:
                possible += 1
        return ans % MOD
            
            
        
        