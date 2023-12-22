class Solution:
    def maxScore(self, s: str) -> int:
    
        ind = 0
        n = len(s)
        pref = [] 
        zeros = 0
        ones = 0
        
        for char in s:
            if char == "0":
                zeros += 1
            pref.append(zeros)
            
        
        for ind in range(n - 1, -1, -1):
            pref[ind] += ones
            if s[ind] == "1":
                ones += 1
         
        
        return max(pref[:-1])
        