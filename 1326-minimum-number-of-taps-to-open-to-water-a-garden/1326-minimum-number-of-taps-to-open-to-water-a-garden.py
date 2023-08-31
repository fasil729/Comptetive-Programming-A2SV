class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        taps = []
        
        for i in range(n + 1):
            taps.append([i - ranges[i], i + ranges[i]])
        
        taps.sort()
        print(taps)
        left = 0
        maxi = 0
        res = 0
        for tap in taps:
            if tap[0] <= left:
                maxi = max(maxi, tap[1])
            else:
                left = maxi
                res += 1
                if tap[0] <= left:
                    maxi = max(maxi, tap[1])
                else:
                    return -1
            if maxi >= n:
                return res + 1
    
        return -1
                
                
            
        