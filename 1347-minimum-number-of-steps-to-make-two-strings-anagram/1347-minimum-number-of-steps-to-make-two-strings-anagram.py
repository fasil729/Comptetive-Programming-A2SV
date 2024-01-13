class Solution:
    def minSteps(self, s: str, t: str) -> int:
        
        count_s = Counter(s)
        count_t = Counter(t)
        ans = 0
        n = len(s)
        
        for char, val in count_s.items():
            ans += min(val, count_t.get(char, 0))
            
        return n - ans
            
            

        
        